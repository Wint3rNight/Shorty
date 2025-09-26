from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login,logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import URLForm, CustomUserCreationForm, UserUpdateForm 
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import F
from .models import ShortenedURL

def home_view(request):
    if request.method=='POST':
        form=URLForm(request.POST)
        if form.is_valid():
            original_url=form.cleaned_data['url']
            url_object = ShortenedURL(original_url=original_url)
            if request.user.is_authenticated:
                url_object.user = request.user
            url_object.save()            
            url_object.generate_and_save_short_code()            
            context={
                'short_code':url_object.short_code,
                'short_url':request.build_absolute_uri(f'{url_object.short_code}'),
                'original_url': url_object.original_url, 
                'click_count': url_object.click_count,
            }
            return render(request,'shortener/success.html',context)
    else:
        form=URLForm()
    return render(request,'shortener/home.html',{'form':form})

def redirect_view(request,short_code):
    url_entry=get_object_or_404(ShortenedURL,short_code=short_code)
    ShortenedURL.objects.filter(pk=url_entry.pk).update(click_count=F('click_count')+1)
    return HttpResponseRedirect(url_entry.original_url)

def details_view(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    context = {
        'entry': url_entry
    }
    return render(request, 'shortener/details.html', context)
    
def register_view(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('shortener:home')
    else:
        form=CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def dashboard_view(request):
    user_links = ShortenedURL.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'links': user_links
    }
    return render(request, 'shortener/dashboard.html', context)

@login_required
def delete_selected_urls_view(request):
    if request.method == 'POST':
        url_ids_to_delete = request.POST.getlist('url_ids')
        ShortenedURL.objects.filter(id__in=url_ids_to_delete, user=request.user).delete()
    return redirect('shortener:dashboard')

@login_required
def delete_account_view(request):
    if request.method=='POST':
        user=request.user
        logout(request)
        user.delete()
        return redirect('shortener:home')
    return render(request, 'shortener/delete_account_confirm.html')

@login_required
def profile_view(request):
    if request.method=='POST':
        form=UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('shortener:profile')
    else:
        form=UserUpdateForm(instance=request.user)
    context={
        'form': form
    }
    return render (request,'shortener/profile.html',context)


from django.contrib import admin
from django.urls import path, include, reverse_lazy

from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(
        'accounts/password_change/done/',
        RedirectView.as_view(pattern_name='shortener:home'),
        name='password_change_done'
    ),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', include('shortener.urls')),
]
from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('details/<str:short_code>/', views.details_view, name='details'),
    path('delete-selected/', views.delete_selected_urls_view, name='delete_selected'),
    path('account/delete/', views.delete_account_view, name='delete_account'),
    path('profile/', views.profile_view, name='profile'),
    path('<str:short_code>', views.redirect_view, name='redirect'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_session_view, name='login_session'),  # Redirect root to login session page
    path('login-session/', views.login_session_view, name='login_session'),
    path('set_session/', views.set_session_view, name='set_session'),
    path('session_created/', views.session_created_view, name='session_created'),
    
    path('login-cookie/', views.login_cookie_view, name='login_cookie'),
    path('set_cookie/', views.set_cookie_view, name='set_cookie'),
    path('cookie_created/', views.cookie_created_view, name='cookie_created'),
]
from . import views
from django.urls import path


urlpatterns = [
    path('signup', views.signup_view, name='sign_up'),
    path('verify-user', views.verify_user_view, name='verify_user'),
    path('login', views.login_view, name='login'),
    path('password-reset', views.password_reset_view, name='password_reset'),
    path('password-reset-confirm', views.password_reset_confirm_view, name='password_reset_confirm'),
]
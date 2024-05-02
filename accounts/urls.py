from . import views
from django.urls import path


urlpatterns = [
    path('signup', views.signup_view, name='sign_up'),
    path('verify-user', views.verify_user_view, name='verify_user'),
    path('login', views.login_view, name='login'),
    path('password-reset', views.password_reset_view, name='password_reset'),
    path('password-reset-confirm', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('users', views.get_all_users_view, name='info_on_all_users'),
    path('u/<str:uid>/update', views.update_user_view, name='update_user_info'),
    path('u/<str:uid>/delete', views.delete_user_view, name='delete_user'),
    path('u/search', views.search_user_view, name='search_users'),
    path('u/<str:uid>', views.user_info_view, name='user_info'),
]
from django.urls import path
from .views import user_login,dashboard,user_register
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('profile/', dashboard, name='profile'),
    path('register/', user_register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(), name='password_reset_complete'),  
]
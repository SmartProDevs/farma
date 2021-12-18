from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login_page, name='login-page'),
    path('logout/', login_page, name='logout_page'),
    path('create/', create_user, name='create_user'),
    path('register/', register_page, name='register-page'),
]
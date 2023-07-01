from user.views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register')
]

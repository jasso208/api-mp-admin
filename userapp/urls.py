from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views.RegistrationView import RegistrationView

urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',RegistrationView.registration_view,name="register")
]
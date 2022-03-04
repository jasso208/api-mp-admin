from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views.RegistrationView import RegistrationView
from .views.UserView import UserView
urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',RegistrationView.registration_view,name="register")    ,
    
    path('get-user-session',UserView.get_user_session,name="get-user-session")
]
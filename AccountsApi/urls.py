from django.urls import path
from AccountsApi.views import UserRegistration,Login,GetOrUpdateUser,DeleteUser,UserDetails
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('registration/', csrf_exempt(UserRegistration.as_view()), name='user_registration'),
    path('login/', csrf_exempt(Login.as_view()), name='user_login'),
    path('user_details/', csrf_exempt(UserDetails.as_view()), name='user_details'),
    path('delete_user/', csrf_exempt(DeleteUser.as_view()), name='delete_user'),
    path('users/', csrf_exempt(GetOrUpdateUser.as_view()), name='users'),
]
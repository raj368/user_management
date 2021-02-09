from django.urls import path
from AccountsApi.views import UserRegistration,Login,HelloView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('registration/', csrf_exempt(UserRegistration.as_view()), name='user_registration'),
    path('login/', csrf_exempt(Login.as_view()), name='user_login'),
    path('hello/', HelloView.as_view(), name='hello'),
]
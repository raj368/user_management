from AccountsApi.auth.login import login_view
from AccountsApi.auth.signup import signup_view
from AccountsApi.crud import all_user,update_user,delete_user,user_details
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from AccountsApi.backend import SafeJWTAuthentication
from django.views import View


class Login(View):
    def post(self, request):
        return login_view(request)

class UserRegistration(View):
    def post(self, request):
        return signup_view(request)

    def get(self,request):
        return all_user(request)

class GetOrUpdateUser(View):
    def get(self,request):
        return all_user(request)

    def post(self, request):
        return update_user(request)

class DeleteUser(View):
    def post(self, request):
        return delete_user(request)

class UserDetails(View):
    def post(self, request):
        return user_details(request)


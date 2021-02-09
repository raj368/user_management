from AccountsApi.login import login_view
from django.views import View
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from AccountsApi.utils import generate_access_token, generate_refresh_token
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from AccountsApi.models import User
from AccountsApi.serializers import RegistrationSerializer


class Login(View):
    def post(self, request):
        return login_view(request)


class UserRegistration(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.filter(username=serializer.data.get('username')).first()
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        return Response(
            {
                'access_token': access_token,
                'refresh_token':refresh_token
            },
            status=status.HTTP_201_CREATED,
        )


class HelloView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
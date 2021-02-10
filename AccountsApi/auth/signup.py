from rest_framework.response import Response
from rest_framework import exceptions
from AccountsApi.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from AccountsApi.utils import generate_access_token, generate_refresh_token
from rest_framework import status
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_view(request):
    phone_number = request.data.get('phone_number', '')
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    DOB = request.data.get('dob')
    marital_status = request.data.get('marital_status')
    resident_address = request.data.get('resident_address')
    gender = request.data.get('gender')
    role = request.data.get('role')

    if phone_number:
        if len(phone_number) != 10:
            return Response({
                'error': 'Phone number is invalid!!'
            }, 400)

    if None in [username,password]:
        raise exceptions.AuthenticationFailed(
            'username and password required')

    if None in [email]:
         return Response({
            'error': 'email required!!'
        }, 400)

    if User.objects.filter(username=username):
        return Response({
            "Error":"User Already Exist"
        })

    if role == "ADMIN":
        User.objects.create_superuser(username=username,email=email,password=password,
                phone_number=phone_number,dob=DOB,
                resident_address=resident_address,role=User.Role.ADMIN)

    elif role not in ["ADMIN"]:
        User.objects.create_user(username=username,email=email,password=password,
                phone_number=phone_number,dob=DOB,
                resident_address=resident_address)

    user = User.objects.filter(username=username).first()            
    
    if role == "INFLUENCER":
        user.role=User.Role.INFLUENCER      
    elif role == "PARTNER":
        user.role=User.Role.PARTNER
    else:
        user.role=User.Role.USER
        

    if gender == 'Male':
        user.gender = User.Gender.MALE
    elif gender == 'Female':
        user.gender = User.Gender.FEMALE
    else:
        user.gender = User.Gender.OTHERS
    
    if marital_status == 'Married':
        user.marital_status = User.MaritalStatus.MARRIED
    elif marital_status == 'Single':
        user.marital_status = User.MaritalStatus.SINGLE
    elif marital_status == 'Separated':
        user.marital_status = User.MaritalStatus.SEPARATED
    elif marital_status == 'Divorced':
        user.marital_status = User.MaritalStatus.DIVORCED
    else :
        user.marital_status = User.MaritalStatus.OTHERS

    user.save()

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    return Response({
        'success' : 'True',
        'access_token': access_token,
        'refresh_token':refresh_token,
    })
    
    return response





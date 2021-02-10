from rest_framework.response import Response
from rest_framework import exceptions
from AccountsApi.models import User
from rest_framework.decorators import api_view, permission_classes
from AccountsApi.utils import generate_access_token, generate_refresh_token
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
import json


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def all_user(request):
    final_res = []
    response = User.objects.all().values('id', 'username', 'phone_number', 'email',)
    final_res.append(response)

    if final_res:
        final_res = final_res
    else:
        final_res = {'status': 'false', 'message': 'blank!!!'}
    return Response(final_res)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_user(request):
    try:
        user_id = int(request.data.get('id'))
    except:
        return Response({'error': 'user_id is a required parameter!!'}, 400)

    update_json_value = request.data.get('update_value')
    
    if not update_json_value:
        return Response({'error': 'Update value is a required parameter!!'}, 400)

    update_value = json.loads(update_json_value)

    try:
        user_update = User.objects.filter(id=user_id).update(**update_value)
   
    except IntegrityError as e:
        if 'email' in e.args[0]:
            return Response({'error': 'Email Id already exists!!'}, 409)
        if 'phone_number' in e.args[0]:
            return Response({'error': 'phone_number already exists!!'}, 409)
    except:
        return Response({'error': "Please Check all details!"}, 400)
    return Response({'message': "User updated successfully!"}, 200)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def delete_user(request):
    try:
        user_id = int(request.data.get('id'))
    except:
        return Response({'error': 'user_id is a required parameter!!'}, 400)
    try:
        user = User.objects.filter(id=user_id)[0]
        user.delete()
   
    except:
        return Response({'error': "User not found!"}, 400)
    return Response({'message': "User deleted successfully!"}, 200)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def user_details(request):
    try:
        user_id = int(request.data.get('id'))
    except:
        return Response({'error': 'user_id is a required parameter!!'}, 400)

    try:
        user = User.objects.filter(id=user_id)[0]
        if user:
            user_details = User.objects.filter(id=user_id).values( 'username', 'phone_number', 'email','dob','marital_status','resident_address','gender','role')
            return Response(user_details)
        else:
            return Response({'error': "User not found!"}, 400)
    except:
        return Response({'error': "User not found!"}, 400)
    
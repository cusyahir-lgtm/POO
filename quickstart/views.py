from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


user = {
    "username": "yayir",
    "name": "Yahir",
    "password": "123",
    "email": "cusyahir@gmail.com",
    "password": "123",
    "birth_day": "2010-01-27",
    "phone": "8441734567"
}

@api_view(["GET"])
def get_user(request):
    data = UserSerializer(user).data
    birth = data['birth_day']
    return Response(data)


@api_view(["POST"])
def create_user(request):
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    

from quickstart.models import Users

@api_view(["GET"])
def get_users(request):
    users = Users.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)
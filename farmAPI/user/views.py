from django.contrib.auth import get_user_model
User = get_user_model()
from . serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        try:
            data = request.data

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            is_farmer = data['is_farmer']

            if is_farmer == 'True':
                is_farmer = True
            else:
                is_farmer = False
            
            if not User.objects.filter(email=email).exists():
                if not is_farmer:
                    User.objects.create_user(name=name,email=email,password=password)
                    return Response({'success':'user created successfully'},status=status.HTTP_201_CREATED)
                else:
                    User.objects.create_farmer(name=name,email=email,password=password)
                    return Response({'success':'farmer account created successfully'},status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'User with this email already exist'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'something went wrong when registering an account'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetriveUserView(APIView):
    def get(self,request):
        try:
            user = request.user
            user = UserSerializer(user)
            return Response({'user':user.data},status=status.HTTP_200_OK)
        except:
            return Response({'error':'something went wrong when retreving user details'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
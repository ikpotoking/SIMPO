from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer

from .models import User



class UserAPIViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class= UserSerializer
    queryset =User.objects.all()
    
class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LoginAPI(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(username) #display on terminal
        print(password) #display on terminal
        print(user) #display on terminal
        if user:
            return Response({
                "name": user.username,
                "token": user.auth_token.key
                
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=400)
            
    
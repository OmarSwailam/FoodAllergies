from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import *

# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            is_doctor = users.objects.get(user=user).is_doctor

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'is_doctor': is_doctor
            })
        else:
            return Response({"Response": "username or password was incorrect"}, status=status.HTTP_401_UNAUTHORIZED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = usersSerializer
    permission_classes = [UserPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        profile_pic = request.data['profile_pic']
        phone = request.data['phone']
        password1 = request.data['password1']
        password2 = request.data['password2']
        try:
            is_doctor = request.data['is_doctor']
        except:
            is_doctor = False
        serializer = usersSerializer(data=request.data)

        if User.objects.filter(username=username).exists():
            return Response({"Response": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(email=email).exists():
            return Response({"Response": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        elif password1 != password2:
            return Response({"Response": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():

                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                nuser = users.objects.create(user=user, profile_pic=profile_pic, phone=phone, is_doctor=is_doctor)

                token = Token.objects.get(user=user).key

                nuser.save()
                user.save()
                return Response({"Token": token}, status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

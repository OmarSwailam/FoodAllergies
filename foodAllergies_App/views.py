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
from . import email_sender
import uuid
from django.shortcuts import get_object_or_404



# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            try :
                is_doctor = users.objects.get(user=user).is_doctor
            except:
                is_doctor = False
            phone = users.objects.get(user=user).phone
            data = {"userdata": {"user_id": user.pk, "first_name":user.first_name, "last_name": user.last_name,
                                 "email": user.email, "phone": phone, "is_doctor":is_doctor, "token": token.key}}
            return Response(data, status=status.HTTP_200_OK)
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

                try:
                    # Generate a unique code and save it in the database
                    code = uuid.uuid4().hex
                    EMAIL_VERIFICATION.objects.create(email=email, code=code)
                    # Send an email to the user's email address containing the code
                    email_sender.send_verification_mail(user, code)
                except Exception as e:
                    print("ERRRRRRORRRRRRRRR", e)

                profile_pic = request.build_absolute_uri(nuser.profile_pic.url)
                data = {"user_id": user.pk, "first_name":first_name, "last_name": last_name,
                                        "email": email, "profile_pic":profile_pic, "phone": phone, }
                return Response({"token": token, "userdata": data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class VerifyEmail_viewSet(viewsets.ModelViewSet):
    queryset = EMAIL_VERIFICATION.objects.all()
    serializer_class = EmailVerificationSerializer
    permission_classes = [RetrieveOnly]
    def retrieve(self, request, pk=None):
        email_verification = get_object_or_404(self.queryset, code=pk)

        # # Check if the user is already verified
        if email_verification.verified:
            return Response({'detail': 'Email already verified'}, status=status.HTTP_302_FOUND)

        email_verification.verified = True
        email_verification.save()
        return Response({"detail":"Email Successfully verified "}, status=status.HTTP_200_OK)
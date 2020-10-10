'''
Created on 2020/09/20

@author: shung
'''
import django_filters
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
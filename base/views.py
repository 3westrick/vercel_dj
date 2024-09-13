from users.models import User
from rest_framework import generics
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import permissions

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    # queryset = User.objects.all()

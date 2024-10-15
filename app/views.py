from rest_framework import permissions
from .serializer import AppSerializer
from .models import Api

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class AppView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    
    queryset = Api.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppViewOne(RetrieveUpdateDestroyAPIView):
    
    queryset = Api.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]
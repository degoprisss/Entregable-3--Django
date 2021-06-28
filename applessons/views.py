from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applessons.models import Applessons
from applessons.serializers import SerializersApplessons


class ApplessonsViewSet(ModelViewSet):
    queryset = Applessons.objects.all()
    serializer_class = SerializersApplessons
    permission_classes = (IsAuthenticated, )


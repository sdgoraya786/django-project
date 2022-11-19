from django.shortcuts import render
from rest_framework import viewsets
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer

"""
Serializer Relations in Django REST Framework 32
Nested Serializer 34
"""

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
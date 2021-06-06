from django.shortcuts import render
from rest_framework import viewsets
from ITSP.models import Team
from .serializers import TeamSerializer

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

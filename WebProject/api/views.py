from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from ITSP.models import Team
from .serializers import TeamSerializer
from .apiformat import api


def apireturn(request):
    return JsonResponse(api)




class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer





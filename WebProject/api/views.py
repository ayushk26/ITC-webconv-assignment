from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from ITSP.models import Team
from .serializers import TeamSerializer



def apireturn(request):
    api = {"data":
               [{"teamID": team.teamID,
                 "teamName": team.teamName,
                 "members": team.members}
                for team in Team.objects.all()]
           }

    return JsonResponse(api)




class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer





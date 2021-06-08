from django.shortcuts import render, HttpResponse
from .models import Team
import requests
import json

def index(request):
    #teams = Team.objects.all()
    teams = requests.get('http://127.0.0.1:8000/api/json/')
    teams = teams.json()
    teams = teams['data']
    return render(request,'index.html',{'teams':teams})

def singleteam(request,pk):

    teams = requests.get('http://127.0.0.1:8000/api/json/')
    teams = teams.json()
    teams = teams['data']
    team = 0

    if pk != 'admin' and pk != 'api':
        #team = Team.objects.get(teamID=pk)
        for i in teams:
            if i["teamID"] == pk :
                team = i
                break


        return render(request,'single.html',{'team':team})



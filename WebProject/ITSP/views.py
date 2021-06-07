from django.shortcuts import render, HttpResponse
from .models import Team
import requests
from .string_to_list import Convert
import json

def index(request):
    #teams = Team.objects.all()
    teams = requests.get('http://127.0.0.1:8000/api/team/?format=json')
    teams = teams.json()
    return render(request,'index.html',{'teams':teams})

def singleteam(request,pk):

    teams = requests.get('http://127.0.0.1:8000/api/team/?format=json')
    teams = teams.json()
    team = 0
    members =0

    if pk != 'admin' and pk != 'api':
        #team = Team.objects.get(teamID=pk)
        for i in teams:
            if i["teamID"] == pk :
                team = i
                members = team["members"]
                members = Convert(members[1:-1])
                break
        return render(request,'single.html',{'team':team,'members':members})



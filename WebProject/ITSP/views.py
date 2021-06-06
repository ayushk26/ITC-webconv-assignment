from django.shortcuts import render, HttpResponse
from .models import Team
import requests
import json

def index(request):
    #teams = Team.objects.all()
    teams = requests.get('http://127.0.0.1:8000/api/team/?format=json')
    teams = teams.json()
    return render(request,'index.html',{'teams':teams})

def singleteam(request,pk):
    def Convert(string):
        li = list(string.split(", "))
        for item in li:
            i = li.index(item)
            li[i] = item[1:-1]
        return li
    teams = requests.get('http://127.0.0.1:8000/api/team/?format=json')
    teams = teams.json()

    if pk != 'admin' and pk != 'api':
        #team = Team.objects.get(teamID=pk)
        for i in teams:
            if i["teamID"] == pk :
                team = i
                members = team["members"]
                members = Convert(members[1:-1])
                break
        return render(request,'single.html',{'team':team,'members':members})



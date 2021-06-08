from ITSP.models import Team

api = {"data":
           [{"teamID": team.teamID ,
             "teamName": team.teamName,
             "members": team.members}
            for team in Team.objects.all()]
       }

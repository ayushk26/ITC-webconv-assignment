from rest_framework import serializers
from ITSP.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('teamID','teamName','members')
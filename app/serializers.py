from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import ArmyList, Unit, ListEntry

class ArmyListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ArmyList
        fields = ('url', 'id', 'name', 'faction', 'points', 'created', 'owner', 'rating', 'votes')

class UnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Unit
        fields = ('url', 'id', 'name', 'utype', 'faction', 'points', 'allowance', 'attachments')
        extra_kwargs = {'attachments': {'many': True, 'queryset': Unit.objects.all()}}

class ListEntrySerializer(serializers.ModelSerializer):
    upk = serializers.ReadOnlyField(source='unit.pk')
    uname = serializers.ReadOnlyField(source='unit.name')
    utype = serializers.ReadOnlyField(source='unit.utype')
    upoints = serializers.ReadOnlyField(source='unit.points')
    uallowance = serializers.ReadOnlyField(source='unit.allowance')
    attachments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListEntry
        fields = ('pk', 'url', 'unit', 'upk', 'uname', 'utype', 'upoints', 'uallowance', 'attachments', 'armylist', 'attached')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    armylists = serializers.HyperlinkedRelatedField(many=True, view_name='armylist-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'username', 'armylists')

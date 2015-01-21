from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import ArmyList, Unit, ListEntry

class ArmyListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    units = serializers.HyperlinkedRelatedField(many=True, view_name='unit-detail', queryset=Unit.objects.all())

    class Meta:
        model = ArmyList
        fields = ('url', 'name', 'faction', 'points', 'created', 'owner', 'units', 'rating', 'votes')

class UnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Unit
        fields = ('url', 'name', 'utype', 'faction', 'points', 'allowance', 'attach')
        extra_kwargs = {'attach': {'many': True, 'queryset': Unit.objects.all().filter(utype='UN')}}

class ListEntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ListEntry
        fields = ('unit', 'armylist', 'attached')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    armylists = serializers.HyperlinkedRelatedField(many=True, view_name='armylist-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'username', 'armylists')

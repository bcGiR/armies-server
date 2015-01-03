from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import ArmyList, Unit

class ArmyListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    units = serializers.HyperlinkedRelatedField(many=True, view_name='unit-detail', queryset=Unit.objects.all())

    class Meta:
        model = ArmyList
        fields = ('url', 'name', 'faction', 'points', 'created', 'owner', 'units')

class UnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Unit
        fields = ('url', 'name', 'utype')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    armylists = serializers.HyperlinkedRelatedField(many=True, view_name='armylist-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'username', 'armylists')

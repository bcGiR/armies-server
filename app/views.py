from app.serializers import ArmyListSerializer, UnitSerializer, UserSerializer, ListEntrySerializer
from app.models import ArmyList, Unit, ListEntry
from django.contrib.auth.models import User
from rest_framework import viewsets
import datetime

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class ArmyListViewSet(viewsets.ModelViewSet):
    serializer_class = ArmyListSerializer

    def get_queryset(self):
        qs = ArmyList.objects.all()

        faction = self.request.QUERY_PARAMS.get('faction', None)
        points = self.request.QUERY_PARAMS.get('points', None)

        if faction is not None:
            qs = qs.filter(faction=faction)

        if points is not None:
            qs = qs.filter(points=points)

        return qs

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            owner = self.request.user
        else:
            owner = None
        serializer.save(owner=owner,
                created=datetime.date.today(),
                rating=0,
                votes=0)

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer

    def get_queryset(self):
        qs = Unit.objects.all()

        faction = self.request.QUERY_PARAMS.get('faction', None)
        utype = self.request.QUERY_PARAMS.get('type', None)

        if faction is not None:
            qs = qs.filter(faction=faction)

        if utype is not None:
            qs = qs.filter(utype=utype)

        return qs

class ListEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ListEntrySerializer
    queryset = ListEntry.objects.all()

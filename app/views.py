from app.serializers import ArmyListSerializer, UnitSerializer, UserSerializer
from app.models import ArmyList, Unit
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
        serializer.save(owner=self.request.user,
                created=datetime.date.today())

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

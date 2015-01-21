from django.conf.urls import url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'armylists', views.ArmyListViewSet, base_name='armylist')
router.register(r'units', views.UnitViewSet, base_name='unit')
router.register(r'listentry', views.ListEntryViewSet, base_name='listentry')

urlpatterns = [
        url(r'^api/', include(router.urls)),
]

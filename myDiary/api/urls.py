from django.urls import path, include
from .views import EntriesView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Entries', EntriesView)


urlpatterns = [
    path('', include(router.urls)),
]
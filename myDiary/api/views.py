from django.shortcuts import render
from rest_framework import viewsets
from .models import Entries
from .serializers import EntrySerializer


class EntriesView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing entry instances.
    """
    queryset = Entries.objects.all()
    serializer_class = EntrySerializer

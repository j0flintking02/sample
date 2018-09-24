from rest_framework import serializers
from .models import Entries


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ('id', 'title', 'description', 'date_created')

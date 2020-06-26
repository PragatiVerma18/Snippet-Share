from .models import Snip
from rest_framework import serializers

class SnipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snip
        fields = ['title', 'text', 'link_code', 'lang', 'created_at', 'updated_at']
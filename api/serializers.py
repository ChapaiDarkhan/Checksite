from rest_framework import serializers

from checksite.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'url', 'status_code', 'extra_data', 'time']
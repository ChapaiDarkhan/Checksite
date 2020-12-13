from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import SiteSerializer
from checksite.models import Site


class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Site.objects.all().order_by('url')
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated]


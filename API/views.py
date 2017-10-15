from sysOS.workshop.models import JobType
from rest_framework import viewsets
from sysOS.API.serializers import JobTypeSerializer


# Create your views here.

class JobTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows JobTypes to be viewed or edited.
    """
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

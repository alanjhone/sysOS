from rest_framework import serializers
from sysOS.workshop.models import JobType

class JobTypeSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()

	class Meta:
		model = JobType
		fields = ('id', 'name', 'description')
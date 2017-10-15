from django.conf.urls import url, include
from rest_framework import routers
from sysOS.API import views

router = routers.DefaultRouter()

# job types
router.register(r'job_type', views.JobTypeViewSet)




urlpatterns = [
    url(r'^', include(router.urls))
]
# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'testapi', views.testAPIViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('/', include(router.urls)),
    path('testapi/', views.testAPIViewSet),
    path('getCrateDBCluster/', views.getCrateDBCluster),
    path('streamSKTest/', views.streamSSESKTests),
    path('api/iot_mgmt/orgs/3/projects/70/gateways/390/data_dump_index', views.getUnit9Data),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.urls import path,include
from enroll.api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('crud', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]

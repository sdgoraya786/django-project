from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Object
router = DefaultRouter()

# Register StudentModelViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get-token/', obtain_auth_token)
]

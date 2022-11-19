from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_api, name='home'),
    # ------ Browsable API ----
    path('<int:pk>', views.student_api, name='home'),
]

from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name='add_show'),
    path('delete/<int:id>', views.UserDeleteView.as_view(), name='delete'),
    path('update/<int:id>', views.UserUpdateView.as_view(), name='update'),
    # for api
    path('api/', include('enroll.api.urls'))
]

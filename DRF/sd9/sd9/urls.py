from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.StudentList.as_view()),
    ## path('', views.StudentCreate.as_view()),
    ## path('<int:pk>/', views.StudentRetrieve.as_view()),
    ## path('<int:pk>/', views.StudentUpdate.as_view()),
    # path('<int:pk>/', views.StudentDestroy.as_view()),

    ## Retrieve and Update
    # path('<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    ## Retrieve and Destroy
    # path('<int:pk>/', views.StudentRetrieveDestroy.as_view()),

    ## List and Create
    path('', views.StudentListCreate.as_view()),
    ## Retrieve, Update and Destroy
    path('<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]

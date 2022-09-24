from django.urls import path
from fees import views

urlpatterns = [
    path('python/',views.fees_py, name='feespy'),
    path('django/',views.fees_django, name='feesdj'),
    path('php/',views.fees_php, name='feesphp'),
]

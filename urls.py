from django.urls import path
from . import views

urlpatterns = [
    path('homerentalweb/', views.homerentalweb),
]

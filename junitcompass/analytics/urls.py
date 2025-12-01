from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('stats/', views.analyze, name='analyze'),
]
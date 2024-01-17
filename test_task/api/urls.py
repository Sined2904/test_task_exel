from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import СheckView, index

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', index, name='index'),
    path('file/', СheckView.as_view(), name='file'),
]
from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
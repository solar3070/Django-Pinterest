from django.urls import path
from acoountapp.views import hello_world

app_name = "acoountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
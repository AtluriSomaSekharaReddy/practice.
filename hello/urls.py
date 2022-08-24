
from . import views
from django.urls import path
urlpatterns = [
    path ("hello/", views.index,name="hello"),
    path ("hi/hi", views.indexx,name="hello")
]
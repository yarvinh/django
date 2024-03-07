from django.urls import path
from . import views, show

urlpatterns = [
    path("", views.index, name="index"),
    path("show/", show.show, name="show"),
    path("test/", views.test, name='index')
]
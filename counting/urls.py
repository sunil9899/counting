from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("interact/", views.interaction, name="interaction"),
    path("output_window", views.output, name="output"),
    path("about us/", views.abt, name="abt"),
]

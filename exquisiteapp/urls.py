from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("collection/", views.collection, name="collection"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
]

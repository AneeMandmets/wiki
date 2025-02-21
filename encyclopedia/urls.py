from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"), 
    path("newpage", views.newpage, name="newpage"),
    path("save_new_page", views.save_new_page, name="save_new_page"),
    path("random_page", views.random_page, name="random_page"),
    path("editpage/<str:title>", views.editpage, name="editpage"),
    path("save_page", views.save_page, name="save_page")
]

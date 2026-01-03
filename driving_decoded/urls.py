from . import views
from django.urls import path
from .views import dashboard

# add paths to create update and delete here
#links to views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("dashboard/", dashboard, name="dashboard"),
    path("journal/new/", views.new_entry, name="new_entry"),
    path("journal/<int:pk>/edit/", views.edit_entry, name="edit_entry"),
    path("journal/<int:pk>/delete/", views.delete_entry, name="delete_entry"),
]
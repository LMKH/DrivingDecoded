from . import views
from django.urls import path

# add paths to create update and delete here
#links to views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]
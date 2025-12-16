from django.shortcuts import render
from django.views import generic
from .models import Post

#connects to urls.py
# grabs all the data from the database
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "base.html"


def dashboard(request):
    return render(request, "dashboard.html")
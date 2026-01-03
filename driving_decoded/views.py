from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, JournalEntry
from .forms import JournalEntryForm

#connects to urls.py
# grabs all the data from the database
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "base.html"


def dashboard(request):
    entries = JournalEntry.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "dashboard.html", {'entries': entries})

def new_entry(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect("dashboard")
    else:
        form = JournalEntryForm()

    return render(request, "newentry.html", {"form": form})

def edit_entry(request, pk):
    entry = JournalEntry.objects.get(pk=pk)

    # Optional: prevent editing someone else's entry
    if entry.author != request.user:
        return redirect('dashboard')

    if request.method == "POST":
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JournalEntryForm(instance=entry)

    return render(request, "newentry.html", {"form": form})

def delete_entry(request, pk):
    entry = JournalEntry.objects.get(pk=pk)

    # Prevent deleting someone else's entry
    if entry.author != request.user:
        return redirect('dashboard')

    if request.method == "POST":
        entry.delete()
        return redirect('dashboard')

    return render(request, "confirm_delete.html", {"entry": entry})
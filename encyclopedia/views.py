from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util

import markdown2
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(util.get_entry(title)),
        "title": title
    })

def search(request):
    query = request.GET.get('q')
    print(f"Search query: {query}")  # Debugging statement
    if util.get_entry(query):
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(query)),
            "title": query
        })
    else:
        entries = util.list_entries()
        entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })  
    
def newpage(request):
    return render(request, "encyclopedia/newpage.html")

def save_new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            entries = util.list_entries()
            if title in entries:
                return HttpResponse("Page already exists.")
            else:
                util.save_entry(title, content)
                return redirect("entry", title=title)
        else:
            return HttpResponse("Title and content cannot be empty.")
    else:
        return redirect("newpage")

def random_page(request):
    entries = util.list_entries()
    choice = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(util.get_entry(choice)),
        "title": choice
    })

def editpage(request, title):
    return render(request, "encyclopedia/editpage.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def save_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            util.save_entry(title, content)
            return redirect("entry", title=title)
        else:
            return HttpResponse("Title and content cannot be empty.")
    else:
        return redirect("index")
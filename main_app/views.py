from django.shortcuts import render
from django.contrib import messages


def landing_page(request):
    context = {
        "page_title": "landing"
    }
    return render(request, 'main_app/landing.html', context)


def feed(request):
    context = {
        "page_title": "feed"
    }
    return render(request, "main_app/feed.html", context)

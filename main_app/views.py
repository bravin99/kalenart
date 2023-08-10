from django.shortcuts import render, redirect
from main_app.models import Feed
from django.contrib import messages


def landing_page(request):
    context = {
        "page_title": "landing_page"
    }
    return render(request, 'main_app/landing.html', context)


def feed(request):
    posts = Feed.objects.filter(display=True)
    context = {
        "page_title": "feed_page",
        "posts": posts
    }
    return render(request, "main_app/feed.html", context)


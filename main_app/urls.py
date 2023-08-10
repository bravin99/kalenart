from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.landing_page, name="landing"),
    path('feed', views.feed, name="feed"),
    path('feed-detail/<slug:slug>', views.feed_detail, name="feed_detail"),
]

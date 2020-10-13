from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_events", views.all_events, name="all_events"),
    path("all_locations", views.all_locations, name="all_locations"),
    path("search_location", views.search_location, name="search_location"),
    path("search_date", views.search_date, name="search_date"),
    path("<int:description_id>/", views.detail, name="detail"),
    path("<int:description_id>/location/", views.event, name="event"),
    path("<int:description_id>/date/", views.date, name="date"),
    # path("<int:question_id>/votes/", views.votes, name="votes"),
    # path("<int:question_id>/results", views.results, name="results"),
]
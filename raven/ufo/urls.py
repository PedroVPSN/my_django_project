from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:description_id>/", views.detail, name="detail"),
    path("<int:description_id>/location/", views.event, name="event"),
    path("<int:description_id>/date/", views.date, name="date"),
    # path("<int:question_id>/votes/", views.votes, name="votes"),
    # path("<int:question_id>/results", views.results, name="results"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:description_id>/", views.detail, name="detail"),
    # path("<int:question_id>/votes/", views.votes, name="votes"),
    # path("<int:question_id>/results", views.results, name="results"),
]
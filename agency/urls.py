from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
]

app_name = "agency"

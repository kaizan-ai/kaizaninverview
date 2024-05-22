from django.urls import path

from transcripts.views import WorkInteractionEntriesListView


urlpatterns = [
    path(
        "<uuid:work_interaction_pk>/entries/",
        WorkInteractionEntriesListView.as_view(),
        name="work-interaction-entries-list",
    ),
]
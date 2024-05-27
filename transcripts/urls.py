from django.urls import path

from transcripts.views import WorkInteractionEntriesListView, WorkInteractionUpdateView


app_name = "transcripts"

urlpatterns = [
    path(
        "<uuid:work_interaction_pk>/entries/",
        WorkInteractionEntriesListView.as_view(),
        name="work-interaction-entries-list",
    ),
    path(
        "<uuid:pk>/update/",
        WorkInteractionUpdateView.as_view(),
        name="work-interaction-update",
    )
]
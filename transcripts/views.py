from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse
from transcripts.forms import WorkInteractionForm
from transcripts.models import Entry, WorkInteraction
from django.views.generic.list import ListView
from django.views.generic import UpdateView


class WorkInteractionEntriesListView(ListView):
    model = Entry
    template_name = "transcripts/entries_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        return Entry.objects.filter(work_interaction=self.kwargs["work_interaction_pk"])
    

class WorkInteractionUpdateView(UpdateView):
    form_class = WorkInteractionForm
    queryset = WorkInteraction.objects.all()
    template_name = "transcripts/workinteraction_form.html"

    def get_success_url(self) -> str:
        return reverse("transcripts:work-interaction-update", kwargs={"pk": self.object.pk})
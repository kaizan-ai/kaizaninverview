from transcripts.models import Entry
from django.views.generic.list import ListView


class WorkInteractionEntriesListView(ListView):
    model = Entry
    template_name = "transcripts/entries_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        return Entry.objects.filter(work_interaction=self.kwargs["work_interaction_pk"])
from django.forms import ModelForm

from transcripts.models import WorkInteraction


class WorkInteractionForm(ModelForm):
    class Meta:
        model = WorkInteraction
        fields = ["title"]
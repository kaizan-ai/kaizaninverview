from django.db.models import CharField
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField

from kaizaninterview.models import BaseModel


class WorkInteraction(BaseModel):
    title_max_length = 2000
    title = CharField(max_length=title_max_length)

    work_streams = ManyToManyField(
        "work_streams.WorkStream",
        related_name="work_interactions",
        through="WorkInteractionWorkStream",
    )


class Entry(BaseModel):
    work_interaction = ForeignKey(WorkInteraction, on_delete=CASCADE)


class WorkInteractionWorkStream(BaseModel):
    work_interaction = ForeignKey(WorkInteraction, on_delete=CASCADE)
    work_stream = ForeignKey("work_streams.WorkStream", on_delete=CASCADE)

from django.db.models.fields import CharField

from kaizaninterview.models import BaseModel


class WorkStream(BaseModel):
    name_max_length = 200

    name = CharField(max_length=name_max_length)

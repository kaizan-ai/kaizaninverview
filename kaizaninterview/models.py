import uuid

from django.db.models import Model
from django.db.models.fields import DateTimeField, UUIDField


class BaseModel(Model):
    """
    Base model to be used for all kaizan models.
    """

    class Meta:
        abstract = True
        ordering: tuple[str, ...] = ("-created_at", "-updated_at")

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__.lower()}:{str(self.id)}"

from django.db import models
from django.utils import timezone

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=True,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=True,
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=True,
        default=True
    )

    class Meta:
        abstract = True
        managed = True

    def __str__(self):
        return f"{self.__class__.__name__} (ID: {self.id})"

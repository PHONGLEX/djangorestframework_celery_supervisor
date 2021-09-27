from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class Book(models.Model):
    title = models.CharField(_("title"), max_length=225, null=False, db_index=True)
    authors = models.CharField(_("authors"), max_length=225)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
"""
Models required for api app
"""
# django imports
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Content(models.Model):
    """
    Content model to store title information
    """
    title       = models.CharField(null=True, blank=True, max_length=200)
    created_by  = models.CharField(null=True, blank=True, max_length=200)
    timestamp   = models.DateTimeField()
    tag         = models.ForeignKey(
                        to           = 'Tag',
                        on_delete    = models.CASCADE,
                        )

    def save(self, *args, **kwargs):
        # create if not exists
        obj, status = Tag.objects.get_or_create(title=self.title)
        # add foreign key relation
        self.tag    = obj
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    """
    Tag model store all tags
    """
    title = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return str(self.title)

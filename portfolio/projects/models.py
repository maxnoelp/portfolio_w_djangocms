from django.db import models
from djangocms_text.fields import HTMLField
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField


class Choice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectRelease(models.Model):
    publish = models.BooleanField(_("Veröffentlicht"), default=False)
    title = models.CharField(_("Titel"), max_length=100)
    content = HTMLField()
    tags = models.ManyToManyField(_("Tags auswähle"), Choice)
    image_thumbnail = FilerImageField(_("Bild einfügen"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

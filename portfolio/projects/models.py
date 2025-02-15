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
    tags = models.ManyToManyField(Choice, verbose_name=_("Tags auswählen"))
    image_thumbnail = FilerImageField(
        verbose_name="Bild einfügen", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

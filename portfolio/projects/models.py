from django.db import models
from djangocms_text.fields import HTMLField
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin


class Choice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectItemModel(models.Model):
    title = models.CharField(_("Titel eingeben"), max_length=150)
    tag = models.ManyToManyField(Choice, related_name="project_items")
    image = FilerImageField(verbose_name=_("Bild einfügen"), on_delete=models.CASCADE)
    description = HTMLField(_("Content eingeben"))
    repository_link = models.URLField(_("Github Link"))

    def __str__(self):
        return self.title

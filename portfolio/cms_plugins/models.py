from django.db import models
from djangocms_text.fields import HTMLField
from cms.models import CMSPlugin
from django.utils.translation import gettext as _


class AboutModel(CMSPlugin):
    content = HTMLField()
    title = models.CharField(_("Titel eingeben"), max_length=100)

    def __str__(self):
        return self.title

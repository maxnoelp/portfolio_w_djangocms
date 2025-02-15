from django.contrib import admin
from portfolio.projects.models import Choice, ProjectRelease
from django.utils.translation import gettext_lazy as _


class ProjectReleaseAdmin(admin.ModelAdmin):
    list_display = ("title", "publish")
    list_filter = ("title", "publish")
    search_fields = ("title", "tags__name")


admin.site.register(ProjectRelease, ProjectReleaseAdmin)
admin.site.register(Choice)

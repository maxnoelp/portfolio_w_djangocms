from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from portfolio.projects.models import ProjectItemModel, Choice


class ProjectAdminClass(admin.ModelAdmin):
    list_display = ("title", "get_tags", "repository_link")
    list_filter = ("tag",)
    search_fields = ("title", "description")
    ordering = ("title",)
    filter_horizontal = ("tag",)

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tag.all()])

    get_tags.short_description = "Tags"


admin.site.register(ProjectItemModel, ProjectAdminClass)
admin.site.register(Choice)

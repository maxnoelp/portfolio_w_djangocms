from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from portfolio.cms_plugins.models import AboutModel


@plugin_pool.register_plugin
class AboutPlugin(CMSPluginBase):
    model = AboutModel
    name = _("CM About me")
    render_template = "about/about_me.html"
    cache = False
    allowed_children = True

    def render(self, instance, context, placeholder):
        return super().render(instance, placeholder, context)

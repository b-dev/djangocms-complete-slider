from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from djangocms_complete_slider.models import CompleteImageSlide, CompleteSlider, CompleteVideoSlide
from djangocms_complete_slider.settings import app_settings
from djangocms_complete_slider.forms import ImageSlideForm, VideoSlideForm


class CompleteSliderPlugin(CMSPluginBase):
    model = CompleteSlider
    cache = False
    name = _("Slider")
    module = _("CompleteSlider plugin")
    allow_children = True
    child_classes = ["CompleteImageSlidePlugin", "CompleteVideoSlidePlugin"]
    render_template = "djangocms_complete_slider/slider.html"
    fieldsets = (
        (None, {
            "fields": [
                "autoplay",
                "loop"
            ]
        }),
        (_("Advanced settings"), {
            "classes": ("collapse",),
            "fields": [
                "slide",
                "timer",
                "delay",
                "transitionDuration",
                "firstTransition",
                "defaultTransition"
            ]
        })
    )

    def render(self, context, instance, placeholder):
        context = super(CompleteSliderPlugin, self).render(context, instance, placeholder)
        context['app_settings'] = app_settings
        return context


plugin_pool.register_plugin(CompleteSliderPlugin)


class CompleteImageSlidePlugin(CMSPluginBase):
    model = CompleteImageSlide
    cache = False
    name = _("Image Slide")
    module = _("CompleteSlider plugin")
    require_parent = True
    allow_children = False
    parent_classes = ["CompleteSliderPlugin"]
    form = ImageSlideForm
    # if i don't have a render_template, the edit popup in frontend doesn't work.
    # so i put a blank template
    render_template = "djangocms_complete_slider/slide.html"


plugin_pool.register_plugin(CompleteImageSlidePlugin)


class CompleteVideoSlidePlugin(CMSPluginBase):
    model = CompleteVideoSlide
    cache = False
    name = _("Video Slide")
    module = _("CompleteSlider plugin")
    require_parent = True
    allow_children = False
    parent_classes = ["CompleteSliderPlugin"]
    form = VideoSlideForm
    # if i don't have a render_template, the edit popup in frontend doesn't work.
    # so i put a blank template
    render_template = "djangocms_complete_slider/slide.html"

plugin_pool.register_plugin(CompleteVideoSlidePlugin)

from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField, FilerFileField


VEGAS_TRANSITION_CHOICES = (
    ('fade', 'fade'),
    ('fade2', 'fade2'),
    ('slideLeft', 'slideLeft'),
    ('slideLeft2', 'slideLeft2'),
    ('slideRight', 'slideRight'),
    ('slideRight2', 'slideRight2'),
    ('slideUp', 'slideUp'),
    ('slideUp2', 'slideUp2'),
    ('slideDown', 'slideDown'),
    ('slideDown2', 'slideDown2'),
    ('zoomIn', 'zoomIn'),
    ('zoomIn2', 'zoomIn2'),
    ('zoomOut', 'zoomOut'),
    ('zoomOut2', 'zoomOut2'),
    ('swirlLeft', 'swirlLeft'),
    ('swirlLeft2', 'swirlLeft2'),
    ('swirlRight', 'swirlRight'),
    ('swirlRight2', 'swirlRight2'),
    ('burn', 'burn'),
    ('burn2', 'burn2'),
    ('blur', 'blur'),
    ('blur2', 'blur2'),
    ('flash', 'flash'),
    ('flash2', 'flash2'),
)


class CompleteSlider(CMSPlugin):
    slide = models.PositiveIntegerField(verbose_name=_("Index number of initial slide"), default=0, blank=False,
                                        null=False)
    timer = models.BooleanField(verbose_name=_("Display timer bar"), default=False, blank=False, null=False)
    autoplay = models.BooleanField(verbose_name=_("Start the Slideshow automatically"), default=True, blank=False,
                                   null=False)
    loop = models.BooleanField(verbose_name=_("Loop the Slideshow"), default=True, blank=False, null=False)
    delay = models.PositiveIntegerField(verbose_name=_("Delay between slides in milliseconds"), default=5000,
                                        blank=False, null=False)
    transitionDuration = models.PositiveIntegerField(verbose_name=_("Transition duration in milliseconds"),
                                                     default=1000, blank=False, null=False)
    firstTransition = models.CharField(max_length=30, choices=VEGAS_TRANSITION_CHOICES, default='F',
                                       verbose_name=_("Transition of the first slide only"))
    defaultTransition = models.CharField(max_length=30, choices=VEGAS_TRANSITION_CHOICES, default='F',
                                         verbose_name=_("Default transition for all slides"))

    def __str__(self):
        return "Slider"


class CompleteImageSlide(CMSPlugin):
    image = FilerImageField(verbose_name='Image', related_name='slide_images')
    link = models.URLField(verbose_name='Image link', null=True, blank=True)
    slideTransition = models.CharField(max_length=30, choices=VEGAS_TRANSITION_CHOICES, default='F')
    caption = HTMLField(blank=True, null=True)
    # you have to customize the "djangocms_complete_slider/sldier.html" to manage this flag
    hidden_on_mobile = models.BooleanField(default=False)

    def get_url(self):
        return self.image.url if self.image is not None else self.link

    def __str__(self):
        return "ImageSlide: %s" % self.get_url()


class CompleteVideoSlide(CMSPlugin):
    video = FilerFileField(verbose_name='Video')
    poster = FilerImageField(verbose_name='Video Poster', related_name='slide_videos')
    link = models.URLField(verbose_name='Video link', null=True, blank=True)
    slideTransition = models.CharField(max_length=30, choices=VEGAS_TRANSITION_CHOICES, default='F')
    loop = models.BooleanField(verbose_name=_("Loop the video"), default=True, blank=False, null=False)
    mute = models.BooleanField(verbose_name=_("Mute the video"), default=True, blank=False, null=False)
    caption = HTMLField(blank=True, null=True)
    # you have to customize the "djangocms_complete_slider/sldier.html" to manage this flag
    hidden_on_mobile = models.BooleanField(default=False)

    def get_url(self):
        return self.video.url if self.video is not None else self.link

    def __str__(self):
        return "VideoSlide: %s" % self.get_url()

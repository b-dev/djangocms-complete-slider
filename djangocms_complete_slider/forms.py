from django import forms
from django.utils.translation import ugettext_lazy as _
from djangocms_complete_slider import models


class ImageSlideForm(forms.ModelForm):
    class Meta:
        model = models.CompleteImageSlide
        fields = '__all__'

    def clean(self):
        data = super(ImageSlideForm, self).clean()
        if data['image'] is None and (data['link'] is None or data['link'] == ''):
            self.add_error('image', _('Image or link should be provided'))
            self.add_error('link', _('Image or link should be provided'))
        return data


class VideoSlideForm(forms.ModelForm):
    class Meta:
        model = models.CompleteVideoSlide
        fields = '__all__'

    def clean(self):
        data = super(VideoSlideForm, self).clean()
        if data['video'] is None and (data['link'] is None or data['link'] == ''):
            self.add_error('video', _('Image or link should be provided'))
            self.add_error('link', _('Image or link should be provided'))
        return data

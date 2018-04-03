from django.conf import settings

static_url = getattr(settings, 'STATIC_URL', '/static/')
app_settings = getattr(settings, 'COMPLETE_SLIDER', {})
if 'JS_URL' not in app_settings:
    app_settings['JS_URL'] = static_url + 'djangocms_complete_slider/js/vegas.js'
if 'CSS_URL' not in app_settings:
    app_settings['CSS_URL'] = static_url + 'djangocms_complete_slider/css/vegas.min.css'

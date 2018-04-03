# djangocms-complete-slider

A complete slider plugin for Django CMS

djangocms-complete-slider can uses both [Vegas Background Slider](https://vegas.jaysalvat.com/)([MIT License](https://github.com/jaysalvat/vegas/blob/master/LICENSE.md))
or [FlexSlider](https://github.com/woocommerce/FlexSlider) inside.

## How to use pugin

1. Install through pip:

```bash
pip install djangocms-complete-slider
```

2. Add `djangocms_complete_slider` to your `INSTALLED_APPS` setting

3. Enjoy Complete Slider in placeholder

Plugin settings description could be found at [Vegas settings documentation](http://vegas.jaysalvat.com/documentation/settings/)


## Customize css and js locations

You can declare `COMPLETE_SLIDER` variable in your django settings with following optional fields:

* `JS_URL` - specify URL to custom Vegas JS file. By default value is `STATIC_URL + 'djangocms_complete_slider/js/vegas.min.js'`

* `CSS_URL` - specify URL to custom Vegas CSS file. By default value is `STATIC_URL + 'djangocms_complete_slider/css/vegas.min.css'`

So, your final config could looks like:

```python
COMPLETE_SLIDER = {
    "JS_URL": "<URL TO YOUR CUSTOM VEGAS JS>",
    "CSS_URL": "<URL TO YOUR CUSTOM VEGAS CSS>"
}
```

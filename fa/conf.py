from django.conf import settings as django_settings

# Default settings
_FONT_AWESOME_DEFAULTS = {

    # The url to load Font Awesome CSS
    'url': '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css',

    # The HTML tag to use
    'tag': 'i',

}


# Settings dict
FONT_AWESOME = {}

# Start with defaults
FONT_AWESOME.update(_FONT_AWESOME_DEFAULTS)

# Apply user settings from conf.settings
FONT_AWESOME.update(getattr(django_settings, 'FONT_AWESOME', {}))

=================
djangocms-section
=================

Section is a DjangoCMS plugin for displaying a section consisting of a FilerImage and TextPlugin instances.
The app can be configured to offer multiple layouts to the user.

Requires `django-filer` and `easy_thumbnails`.

Quick start
-----------
1. Install with your favorite tool
2. Add `'section'` to `INSTALLED_APPS`.
3. Configure a `'preview'` thumbnail alias for easy_thumbnails if you're going to use the default template like so::
    THUMBNAIL_ALIASES = {
        'preview': {
            'size': (320, 150),
            'crop': 'smart',
        },
    }

4. Enjoy adding a Section plugin to a page.

Custom layouts
--------------
You can add as many layout templates as you desire. See `templates/section/default.html` for an example.
Don't forget to render the placeholder for the text plugins.
The templates have to be enabled in the settings::
    SECTION_STYLE_CHOICES = (
        ('default', _('default')),
        ('lightbox', _('with lightbox')),
    )

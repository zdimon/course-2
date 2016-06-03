##Django toolbar

https://django-debug-toolbar.readthedocs.io/en/1.4/installation.html

###Instalation

    pip install django-debug-toolbar


###Configuration

    INSTALLED_APPS = (
        # ...
        'django.contrib.staticfiles',
        # ...
        'debug_toolbar',
    )

    STATIC_URL = '/static/'


The Debug Toolbar will automatically adjust a few settings 
when you start the development server, provided the DEBUG setting is True.


    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]





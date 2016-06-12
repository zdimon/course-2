##Registration

    pip install django-registration==1.0

    

Add link

    <a id="registration" class="btn btn-success" href="{% url 'registration_register' %}">Registration</a>

Add urls

    url(r'^accounts/', include('registration.backends.default.urls')),

Setting

    ACCOUNT_ACTIVATION_DAYS = 7

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/email-messages/'

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'mail.pressinfo.am'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'noreply@pressinfo.am'
    EMAIL_HOST_PASSWORD = '***'
    DEFAULT_FROM_EMAIL = 'pressinfo.am@gmail.com'


Copy templates.







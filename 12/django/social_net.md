##Social networks

    pip install django-social-auth==0.7.28


    INSTALLED_APPS = (
        ...
        'social_auth'
    )



    AUTHENTICATION_BACKENDS = (
        'social_auth.backends.twitter.TwitterBackend',
        'social_auth.backends.facebook.FacebookBackend',
        'social_auth.backends.google.GoogleOAuthBackend',
        'social_auth.backends.google.GoogleOAuth2Backend',
        'social_auth.backends.google.GoogleBackend',
        'social_auth.backends.yahoo.YahooBackend',
        'social_auth.backends.browserid.BrowserIDBackend',
        'social_auth.backends.contrib.linkedin.LinkedinBackend',
        'social_auth.backends.contrib.disqus.DisqusBackend',
        'social_auth.backends.contrib.livejournal.LiveJournalBackend',
        'social_auth.backends.contrib.orkut.OrkutBackend',
        'social_auth.backends.contrib.foursquare.FoursquareBackend',
        'social_auth.backends.contrib.github.GithubBackend',
        'social_auth.backends.contrib.vk.VKOAuth2Backend',
        'social_auth.backends.contrib.live.LiveBackend',
        'social_auth.backends.contrib.skyrock.SkyrockBackend',
        'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
        'social_auth.backends.contrib.readability.ReadabilityBackend',
        'social_auth.backends.contrib.fedora.FedoraBackend',
        'social_auth.backends.OpenIDBackend',
        'django.contrib.auth.backends.ModelBackend',
    )




    urlpatterns = patterns('',
        ...
        url(r'', include('social_auth.urls')),
        ...
    )




    TWITTER_CONSUMER_KEY         = ''
    TWITTER_CONSUMER_SECRET      = ''
    FACEBOOK_APP_ID              = ''
    FACEBOOK_API_SECRET          = ''
    LINKEDIN_CONSUMER_KEY        = ''
    LINKEDIN_CONSUMER_SECRET     = ''
    ORKUT_CONSUMER_KEY           = ''
    ORKUT_CONSUMER_SECRET        = ''
    GOOGLE_CONSUMER_KEY          = ''
    GOOGLE_CONSUMER_SECRET       = ''
    GOOGLE_OAUTH2_CLIENT_ID      = ''
    GOOGLE_OAUTH2_CLIENT_SECRET  = ''
    FOURSQUARE_CONSUMER_KEY      = ''
    FOURSQUARE_CONSUMER_SECRET   = ''
    VK_APP_ID                    = ''
    VK_API_SECRET                = ''
    LIVE_CLIENT_ID               = ''
    LIVE_CLIENT_SECRET           = ''
    SKYROCK_CONSUMER_KEY         = ''
    SKYROCK_CONSUMER_SECRET      = ''
    YAHOO_CONSUMER_KEY           = ''
    YAHOO_CONSUMER_SECRET        = ''
    READABILITY_CONSUMER_SECRET  = ''
    READABILITY_CONSUMER_SECRET  = ''



    LOGIN_URL          = '/login-form/'
    LOGIN_REDIRECT_URL = '/logged-in/'
    LOGIN_ERROR_URL    = '/login-error/'



<a href="{% url "socialauth_begin" "vk-oauth" %}"> <img src="/static/images/vk.jpg" /> </a>
<a href="{% url "socialauth_begin" "facebook" %}"> <img src="/static/images/fb.png" /> </a>
<a href="{% url "socialauth_begin" "google-oauth2" %}"> <img src="/static/images/google.png" /> </a>







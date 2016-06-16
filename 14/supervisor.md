###Supervisor

    apt-get install python-supervisor


###Scripts

    #!/bin/bash
    cd /home/webmaster/ngchat_ve/angular-chat/djapp
    source ../../bin/activate
    python manage.py celeryd



    nano /etc/supervisor/conf.d/site.conf

    [program:celery]
    command=/home/webmaster/ngchat_ve/angular-chat/djapp/celeryd.sh
    directory=/home/webmaster/ngchat_ve/angular-chat/djapp
    environment=PATH="/home/webmaster/ngchat_ve"
    user=webmaster
    autostart=true
    autorestart=true

    [program:celerybeat]
    command=/home/webmaster/ngchat_ve/angular-chat/djapp/beat.sh
    directory=/home/webmaster/ngchat_ve/angular-chat/djapp
    environment=PATH="/home/webmaster/ngchat_ve"
    user=webmaster
    autostart=true
    autorestart=true





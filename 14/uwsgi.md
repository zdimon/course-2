##UWSGI

    apt-get install uwsgi uwsgi-plugin-python

###Create ini file

    sudo nano /etc/uwsgi/apps-enabled/site.ini

    [uwsgi]
    thread          = 3
    master          = true
    processes       = 2
    module          = blog.wsgi
    chdir           = /home/zdimon/www/course-2/blog
    socket          = /tmp/blog.sock
    logto           = /home/zdimon/www/course-2/blog.uwsgi.log
    vacuum          = true
    max-requests    = 5000
    buffer-size     = 32768
    chmod-socket    = 777
    plugins         = python
    home            = /home/zdimon/www/course-2/ve
    uid = zdimon
    gid = zdimon
    

###Restarting uwsgi server

    sudo service uwsgi restart

###Create vhost block in nginx file


    server {
        listen      80;
        server_name blog.local.com;
        access_log  /home/zdimon/www/course-2/blog/nginx.log;
        location / {
               uwsgi_pass      unix:///tmp/blog.sock;
               include         uwsgi_params;
               #proxy_pass http://127.0.0.1:8888;
        }
        location /static {
            alias /home/zdimon/www/course-2/blog/static;
        }
       location /media {                                                                                                                                                           
            alias /home/zdimon/www/course-2/blog/media;                                                                                                                                   
        }   
    }    

##Statistic

    https://github.com/xrmx/uwsgitop


    --stats 127.0.0.1:1717
    --stats /tmp/statsock

    uwsgitop /tmp/stat.sock

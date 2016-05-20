##Nginx

    upstream myappbackend {
                server 127.0.0.1:8882  max_fails=3 fail_timeout=10s;
                server 127.0.0.1:8883  max_fails=3 fail_timeout=10s;
                server 127.0.0.1:8883  max_fails=3 fail_timeout=10s;
        }



    server {
	    listen 80;
	    server_name chatt.marriage-brides.com;
	    access_log /var/log/nginx/chat-webserver.log;


        location / {
        proxy_pass http://myappbackend;
        #proxy_pass http://localhost:8882;
        }



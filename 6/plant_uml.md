##Plant UML. Pelican integration.

Repo

https://github.com/getpelican/pelican-plugins/tree/master/plantuml

### Install JAVA

Check version

    zdimon@desktop:~/www/course-2/pelican-doc$ java -version
    The program 'java' can be found in the following packages:
     * default-jre
     * gcj-4.9-jre-headless
     * gcj-5-jre-headless
     * openjdk-7-jre-headless
     * gcj-4.8-jre-headless
     * openjdk-6-jre-headless
     * openjdk-8-jre-headless
    Try: sudo apt-get install <selected package>

Installing

    sudo apt-get install default-jre


1. Download plantuml.jar from here http://plantuml.com/download.html

2. Move this file to /opt/plantuml/ as root user.

3. Create bash script in /usr/local/bin directory.

    sudo nano /usr/local/bin/plantuml

copypast this content

    #!/bin/bash
    java -jar /opt/plantuml/plantuml.jar ${@}

4. Make this script executable
    
    sudo chmod +x /usr/local/bin/plantuml



5. Clone (download) plugins.
        
    git clone https://github.com/getpelican/pelican-plugins
    mkdir plugins

6. Edit pelicanconf.py

    PLUGIN_PATHS = ['/home/zdimon/www/course-2/pelican-doc/pelican-plugins/']

    PLUGINS = [ "plantuml" ]

 


### Install nodejs npm and bower

    apt-get install nodejs
    apt-get install npm
    npm install -g bower



Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. 


npm - Package manager. Installs, publishes and manages node programs.

bower - A package manager for the web.

                     
### Create file of dependencies bower.json

    {
      "name": "chat",
      "version": "0.0.1",
      "dependencies": {
        "angular": "*",
        "jquery": "*",
        "bootstrap": "*",
        "angular-ui-router": "*",
        "sockjs": "*"
      }
    }

### Create .bowerrc

    {
        "directory" : "static/library/"
    }

### Install js and css libraries.

    bower install

##Bower


###Installation

    sudo apt-get install nodejs
    sudo apt-get install npm
    sudo npm install -g bower

###bower.json

    {
      "name": "article",
      "version": "0.0.1",
      "dependencies": {
        "angular": "1.4.0",
        "jquery": "~1.10.2",
        "bootstrap": "~3.1.1",
        "restangular": "~1.5.1",
        "angular-ui-router": "0.2.0",
        "underscore": "~1.8.3",
        "angular-resource": "1.4.0",
        "angular-cookies": "1.4.0"
      }
    }

###.bowerrc

    {
        "directory" : "static/lib/"
    }

###Installation

    bower install


If you see that error 

/usr/bin/env: node: No such file or directory

You need to create simlink to binary file of the nodejs.

    .. code-block:: bash

        ln -s /usr/bin/nodejs /usr/bin/node




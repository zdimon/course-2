##Distribution

https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

###Requirements for Packaging and Distributing

1. First you have to install pip installer.

2. Install twine

    pip install twine

Twine uses only verified TLS to upload to PyPI in order to protect your login and password from theft.

###Configuring your Project

Create setup.py file which will contain setup() function. 
This file provides a command line interface for packaging tasks.

    python setup.py --help-commands



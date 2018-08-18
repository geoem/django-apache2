## Docker container for Django and Apache2 on Ubuntu

This is my configuration to build a docker container with a demo Django project on Ubuntu system with Apache2.

#### Prerequisites
 * [Docker CE](https://docs.docker.com/install/)
 * [Docker compose](https://docs.docker.com/compose/install/)

#### Key features

  * Container 
    * Based on [ubuntu:latest](https://hub.docker.com/_/ubuntu/) image
    * Container name: *django-apache2*
    * Symbolic links for *python3* and *pip3* are created to run python commands just by typing *python* and *pip* respectively, instead of *python3* and *pip3* at the command line.
    * Default HTTP port 80 is exposed and binded to port 80 on the localhost machine
  * Apache2
    * [WSGIDaemonProcess](https://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIDaemonProcess.html) directive in apache2 configuration file to run Django application and keep python-path inside the *VirtualHost* tag.
  * Django
    * [Django version 2.0](https://docs.djangoproject.com/en/2.0/) framework (requires Python 3.x to run)
    * [Bootstrap 4 template](https://startbootstrap.com/template-overviews/bare/)
    * No superuser account has been activated
    * No migrations have been made
    * DEBUG value is set to *True*
    * No virtualenv is required

#### How to build the container

Open a terminal and navigate to project folder. To build the container simply run (with elevated privileges) the following:
```shell
$ docker-compose up -d --build
```

The "--build" option ensures to rebuild the container when changes at configuration files exist. Once the container is being created, navigate to http://localhost in your browser. The demo site should looks like the following:

![Django demo site](http://georgioudakis.com/images/blog/django_demo_site.gif)

**Start a bash shell inside the running container**

To interact with the running container and start a bash shell execute the following command in a terminal:
```shell
$ docker exec -it --hostaname ubuntu django-apache2 bash
```

#### Author

Manolis Georgioudakis (geoem@mail.ntua.gr)
  
Copyright &copy; 2018
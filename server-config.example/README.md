This is document (most important in this project) about setup uWSGI along with the project


## Structure:

### Simple version

Basic:
For prodution deployment, we need to set up project like this
```
    Browser <--> nginx <--> uWSGI <--> Flask App 
```

Extra
Actually, it can also be:
```
    Browser <--> nginx <--> App
    Browser <--> WSGI <--> App
    Browser <--> App
```
But none of these settings are recommended for deploying in production, so, we go with the basic one.


### Complex version

```                     
                          /------ Node
                         /------ PHP
                        v                                          
    Browser <-------> nginx <--------------> uWSGI <------------> Flask App 
                   Manage server         Manage project       ^---- Flask App (duplicate)
                                                ^       ^       
                                               /|\       \------- Django App       
                                                |         \------ Other App
                                                |
                                            Emperior mode
                                           Server settings (service to auto start)
```

## 0. Install


On linux, install uwsgi and nginx

```
    sudo apt-get install uwsgi nginx
```

uwsgi in also be installed inside a virtual environment by using `pip`:

```
    pip install uwsgi
```


## 1. uWSGI

Set up uWSG basic:

```
[uwsgi]

project= <project-name>             # Project name here (for separate with other project)
uid = <username></username>         # UID, can be consider as a variable
base = /project/path/%(uid)/project         # base folder

chdir = /path/to/project/folder (contain wsgi file) # 
home = /path/to/env

# Run as wsgi file individually
wsgi-file = wsgi.py                 # WSGI file (exportable an app)
callable = app                      # App file exportable

socket = app.sock                   # This is the path to create *.sock file for nginx to pass data

# ...
```

For normal case, you only set some above settings to run uwsgi. There are many other options
for uwsgi. Please see [here](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html) for knowing more about how to set up with uwsgi.


## 2.nginx

Nginx is used for server to communicate with uwsgi.
For other parts of nginx, config like normal.

Setup upstream for nginx like this:


```
# ...
upstream flask {
	
	# use sock file created by uwsgi (with setting socket)
    server unix:///path/to/sock/file/app.sock;
	
}


server {
    #...

    location / {
        uwsgi_pass  flask;                  # Specific flask as uwsgi upstream name above
        include     /etc/nginx/uwsgi_params;
    }

    #...
}

# ...
```
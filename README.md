=======
SmartWok
========

This repository contains the source code for testing SmartWok.

###1.  Setting up development environment###

Creating Virtual Environments:

```
$ sudo apt-get install python-virtualenv
$ cd smartWok_server/
$ virtualenv venv
$ . venv/bin/activate
```

Database Migration:

```
$ python  manage.py  db  upgrade
```

Install flask and extensions:

```
$ pip install -r requirements.txt
```

Start the server:

```
$ python manage.py runserver
```


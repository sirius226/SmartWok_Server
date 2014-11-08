=======
SmartWok
========

This project has become a group project and transmitted to Bitbucket.

I simplely do not duplicate every commits which submitted on the Bitbucket.

So here is only a repository for back-ups.

Details to see at:

https://bitbucket.org/honghanlin/smartwok_server

Deployed version to see at:

http://54.165.160.160/featured


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


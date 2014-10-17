milo
====

[![Code Health](https://landscape.io/github/thefinn93/milo/master/landscape.png)](https://landscape.io/github/thefinn93/milo/master) [![Build Status](https://travis-ci.org/thefinn93/milo.svg)](https://travis-ci.org/thefinn93/milo)

An Interactive Campus Map for the University of Washington Bothell that is built using

| Package | Version |
|:--------:|:-------|
|Python | 3 |
|Flask | 0.10.1 |
|Flask-SQLAlchem | 2.0 |
|Jinja2 | 2.7.3 |
|MarkupSaf | 0.23 |
|SQLAlchemy | 0.9.8 |
|Werkzeug | 0.9.6 |
|itsdangerous | 0.24 |

Install
----
-----------------------------------------------------------------------------

First, create a virtualenv. Run:

```
$ virtualenv -p python3 milo
```

then: 

```
$ cd milo
```

into this repo, and clone the repo inside the folder

```
$ git clone ...
```
Then activate the virtual environment

```
$ source bin/activate
```
For Mac:

```
$ . bin/activate
```

If it worked, it will put you back at a shell without outputting anything, but with the word `(milo)` in front of your prompt.

Now you may install the dependencies. To do so, run

```
$ pip install -r requirements.txt
```

then sit back and let it run.

Once it's all done, you can do

```
$ pip freeze > temp.txt ; diff temp.txt requirements.txt | wc -l ; rm temp.txt
```

If your terminal says 0 then you are good to go!! If it is greater than 0 than something didn't install right. You can just run:
```
pip freeze
```

To see what did install in your environment


### Flask and SQL Alchemy Database Setup

------------------------------------------

Pull down the latest changes from github using 

```
$ git pull
```

Open up two terminal windows/tabs
In one of the terminal windows/tabs type in:

```
$ python milo.py
```
This will launch the server on localhost:5000 in your browser (or 127.0.0.1:5000, it's the same thing) However you will most likely get an Internal Server Error! It's time to setup the database

In the other window/tab launch the Python interpretter

```
$ python
```
Your terminal will now change to the Python interpretter that looks like this

```
>>>
```

Now Let's setup the database by typing in these commands:

```
>>> from milo import db
>>> db.create_all()
```
What this does is create all the tables within the database, although they are empty, they are at least created.


At the moment Users are in here just to play around with the interpretter and database, it will be deleted at a later time, but if you want to practice with the interpretter and the database you can do the following:

If you didn't do the above step you will need to import the db

```
>>> from milo import db
>>> from milo import User
>>> admin = User('admin', 'admin@example.com')
>>> guest = User('guest', 'guest@example.com')
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()
```

If you reload the page on your browser you will now see the users you just added! You can also check within the python interpretter by doing these commands:

```
>>> users = User.query.all()
>>> users
[<User 'admin'>, <User 'guest'>]
```

You can even do fun things such as:

```
>>> users[0].username
'admin'
```



###Misc Stuff

---------------------------------------------------------------------------

Here is a fun little alias you can add to your .bash_profile, .bashrc, (which ever one you have or want to create) to help get to your dev environment faster


```
alias milo='/path/to/milo/virtualenv ; source bin/activate ; cd milo'
```

Example:

```
alias milo='/Users/will/Sites/milo ; source bin/activate ; cd milo'
```

If you have a Mac replace "source" with just the ".". 

What this does is goes to the folder where you set up your virtual env, so this is the folder with the "bin", "include" and "lib" folders. This is also where you clones the milo repo into. So what this alias does is when you just type in milo anywhere in your terminal, it will

1. Go to the virtual folder
2. Activate the virtual environment
3. Then take you into the github folder where all our code is

To find the full path of your virtual folder (in my case /Users/will/Sites/milo) just type in:

```
$ pwd
```
When you are in the virtual folder and it will tell you!

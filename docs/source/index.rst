.. moneyBox documentation master file, created by
   sphinx-quickstart on Thu Nov  5 12:43:40 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to moneyBox's documentation!
====================================

A simple expenses tracker build using Kivy and Firebase.
*(Still in progress)*

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Features
--------

Authentication & Database
^^^^^^^^^^^^^^^^^^^^^^^^^

The backend of the app was build using Firebase and the Firebase API for
authentication and database storage. This was set up with the help of the
`Pyrebase4 <https://github.com/nhorvath/Pyrebase4>`_ library.

**Authentication:** Two methods of authentication where set up, anonymous and
authentication via e-mail and password. This would allow the user to access the
application on multiple devices instead of only locally.

**Database:** Since Firebase databases are non relational and based on a JSon
structure, the storage was designed as follows.

.. image:: img/database_structure.png

As seen in the picture, the database not only stores information about the user
accounts, but also settings and user info. This information can be edited by the
user through the settings screen.

User Interface
--------------

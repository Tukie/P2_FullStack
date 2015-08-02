Nanodegree P2 Tournament Results
================================

Common code for the Relational Databases and Full Stack Fundamentals courses.

Requirements
------------
1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm repository
3. Launch the Vagrant VM

Dependencies and supported Python versions
------------------------------------------
- Python version 2.7.6
- [psycopg2] (#http://initd.org/psycopg/)

Please follow these steps to create the environment until running the unit test

Creating Database
----------------- 
In order to setup the database please start psql with this command:
    psql -f tournament.sql

As an alternative, you can build and access the database by executing ['psql'],
and then followed by 
    \i tournament.sql
By typing ['\q'] we can exit psql program

Development code
----------------
the logic behind the tournament and its database processing are defined in
['tournament.py']

Test
------
Start the test program using:
```python
python tournament_test.py
```

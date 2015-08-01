Nanodegree P2 Tournament Results
================================

Common code for the Relational Databases and Full Stack Fundamentals courses.

Requirements
------------
1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm repository
3. Launch the Vagrant VM

Please follow these steps to create the environment until running the unit test

Creating Database
-----------------
First, to build and access the database we run psql followed by 
\i tournament.sql

By typing \q we can exit psql program 
In order to open and check the database please start psql with this command:
psql -f tournament.sql

Testing
------
Start the test program using:
python tournament_test.py


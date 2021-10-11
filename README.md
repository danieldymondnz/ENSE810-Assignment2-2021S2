# ENSE810-Assignment2-2021S2
The Delivery Monitoring System (DMS). A solution for monitoring driving behaviour and enviromental conditions of a delivery vehicle using a Raspberry Pi Sense HAT and remote MySQL database. Completed as part of Assignment 2 for ENSE810 at AUT.

Co-Authored by danieldymondnz and KyleAM1

## Contents of Repository 

### app
This folder contains the python application for use on the embedded system.

### testing
This folder contains the testing scripts for the database agent:
* `DBAgent_test.py` uses the Python unit testing framework to test methods in the Database Agent.
* `DBAgent_threadTest.py` creates a test environment using a csv file to emulate local data and append records to a MySQL database.

### Web Application
This folder contains the server-side files to host the PHP web application. The files are intended to be used on the same server as the remote database, connected to a MySQL database named "sdmms-db".

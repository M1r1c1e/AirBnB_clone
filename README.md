# AirBnB clone - The console
## Overview:
This is the first step in creating a clone Airbnb web application.
This is done by creating a command-line interface which allows users 
to manage objects on the Airbnb web applictaion.

## Description of the command interpreter:
The command interpreter, also referred to as a shell or CLI (Command-Line Interface), 
is the core component of this project which serves as an interactive interface 
for users to communicate with the system and execute various commands

## Starting point:
This program begins by cloning the repository and then run console.py

## Execution:
### Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

### non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

### Environment:
Python3
### Authors
Miracle Anderson

# Project Video Database

## The idea of the project

This is an app which is storing information about YouTube videos. The app is designed using Model-View-Controller design pattern. The primary implementation uses SQLite Database to store thr data but there is also a possibility to add another way of saving objects. The app also provides a GUI for reading and editting all the data.  

## User Manual

In the main app window there are 3 buttons:
* "Add Video" - enables inserting new record to the database.  
    :warning: Syntax is important:
    * the data should be in dd.mm.yyyy format (e.g. "01.01.2000")
    * key words should be separated by a comma and a space (e.g. "cat, dog" or "horse,") 
    
* "Video Table" - enables viewing all information about  that have been added to the database so far (there are multiple sorting options)
* "Keywords Table" - enables viewing keywords and their corresponding videos that have been added to the database so far (there are multiple sorting options)

## Class Diagram
![](https://i.imgur.com/9qkWovS.png)

## Running the program

### Requirements

It is required to have Python 3.x interpreter installed.

### Required libraries

Firstly, create Virtual Environment, install the required libraries and activate the created Virtual Environment. 

#### Linux
~~~ bash=
python3 -m venv venv
source venv/bin/activate
python3 -m pip install requirements.txt
~~~

#### Windows
~~~ bash=
py -m venv venv
.\venv\Scripts\activate
py -m pip install requirements.txt
~~~

### Start the app

#### Linux
~~~ bash=
python3 ./code/controller.py
~~~

#### Windows
~~~ bash=
py ./code/controller.py
~~~



 


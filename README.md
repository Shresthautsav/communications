Copyright (C) MAY 23, 2021 UTSAV SHRESTHA, HIEP LE, SUJAN DHAKAL, TAKUDZWA MUJURU
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE UTSAV SHRESTHA, HIEP LE, TAKUDZWA MUJU, SUJAN DHAKAL or LAFAYETTE COLLEGE BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Lafayette Communication Project

To run the project, you will have to install few things into your computer. 

1) Django: pip install django
2) psycopg2: pip install psycopg2

Django is required because the project is a django project and we are using various features of
Django like migrations. Psycopg2 is the translator betweeen django and postgres. 

The important files in this repository are:

1) Models.py - Holds all the Django Models which is used to create the database table. 

2) Population files - There are five python scripts in the commands folder. They are:
	1) data_import.py 
	2) interest_import.py
	3) populate_interest.py
	4) populate_majors.py
	5) populate_users.py

3) Data files - There are three files that hold the data that needs to be imported into the database
	1) majors.csv - list of all majors
	2) interest.csv - list of all newsletter interest
	3) final-list.csv - holds info of all the users from survey + scrapping.

Run these files in a sequential order as follows:

    - python3 manage.py data_import "majors.csv"
    - python3 manage.py interest_import "interest.csv"
    - python3 manage.py populate_users "final-list.csv"
    - python3 manage.py populate_majors "final-list.csv"
    - python3 manage.py populate_interests "final-list.csv"

The files that hold the data "majors.csv", "interest.csv", and "final-list.csv" need to be in
the same folder as manage.py for the python script to run properly. 


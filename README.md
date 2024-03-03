# Bucharest Court Trial Management System

Made by Bolohan Stefan-Tudor

### Project Description

This project is a simple web application that allows users to view and manage a list of criminal trials, the laws applied to those trials and who is involved in that trial. The application is built using the Flask micro framework to connect to a MySQL database, where is stored all the information. This is designed to be used by the Bucharest Court.

### Features

- View all trials (with all the information about the trial, including the laws applied to it, the judge, the participants, etc.)
- View all laws
- View all judges
- View all participants on every trial
- View all types of particiapants (plaintiff, defendant, witness, etc.)
- Search based on a certain criteria (e.g. search for all cases that have a certain law applied to them)

For some pages, there is also the possibility to add, edit or delete an entry.

### Installation

1. Clone the repository
2. Install Python to use Flask. To install Flask, you can use the following command:
   ``pip install Flask``
3. Install MySQL
4. Create a database in MySQL and import the .sql file from the repository which is located in the **"Database"** folder
5. Change the database credentials in the config.py file
6. Run the application using the following command:
   ``python app.py``

### Technologies

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript
- Bootstrap

### Footnote

The content of this project is purely fictional, written in Romanian and is not meant to be used in a real court trial management system and. This is a project made for educational purposes only.

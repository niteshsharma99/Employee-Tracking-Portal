

# Employee-Tracking-Portal

The Employee Tracking Portal is a sample web application built using Python and Flask. It provides a user-friendly interface for managing employee information, including creating, viewing, updating, and deleting employee records. The application incorporates authentication functionality using Flask-Login, allowing users to sign up and log in securely.

**####Features######**

**User Registration:** New users can sign up for an account by providing their email address, name, and password.

**User Authentication:** Registered users can log in to the application using their email and password.

**Employee Management:** Once logged in, users can perform various actions related to employee management, such as:
View a list of all employees with their details, including name, gender, address, phone number, salary, and department.
Add a new employee by entering their information.

Edit the details of an existing employee, including their name, gender, address, phone number, salary, and department.
Delete an employee record from the system.

**User Profile:** Users have a profile page where they can view their own information, such as their name and email address.


**######To complete this project, you will need the following###########**

Some familiarity with Python.
Python installed on a local environment.
Knowledge of Basic Linux Navigation and File Management.

This Project was verified with sqlite3 v3.36.0, python v3.9.8, flask v2.0.2, flask-login v0.5.0, and flask-sqlachemy v2.5.1.

Steps to run this project:

**1. Clone this repository**
git clone https://github.com/niteshsharma99/Employee-Tracking-Portal.git

**2. Enable Virtual Env in python -** 
cd Employee-Tracking-Portal/                                                                     
python3 -m venv auth                                                                     
source auth/bin/activate                                                                           
pip install flask flask-sqlalchemy flask-login

**3. Export the Required Variable-**
cd Employee-Tracking-Portal/project                                                                           
export FLASK_APP=.
export FLASK_DEBUG=1

**#If outside from project then run  **
export FLASK_APP=project

**4. If table is mot create then run this below script:**
cd Employee-Tracking-Portal/
python3 dbcreate.py

**5. Run the application**
cd Employee-Tracking-Portal/project
flask run 

**6. After running "flask run" Check the browser on localhost:**
localhost:5000/

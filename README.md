# Employee-Tracking-Portal


Steps to run this project:

1. Clone this repository
git clone https://github.com/niteshsharma99/Employee-Tracking-Portal.git

2. Enable Virtual Env in python - 
cd Employee-Tracking-Portal/flask_auth_scotch
python3 -m venv auth
source auth/bin/activate
pip install flask flask-sqlalchemy flask-login

3. Export the Required Variable-
cd Employee-Tracking-Portal/flask_auth_scotch/project
export FLASK_APP=.
export FLASK_DEBUG=1

#If outside from project then run  
#export FLASK_APP=project

4. If table is mot create then run this below script:
cd Employee-Tracking-Portal/flask_auth_scotch
python3 dbcreate.py

5. Run the application
cd Employee-Tracking-Portal/flask_auth_scotch/project
flask run 

6. After running "flask run" Check the browser on localhost:
localhost:5000/
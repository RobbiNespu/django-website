# Setup the environment
```
$ python3 -m venv venv
```
you can use the following step to activate your virtualenv.
```
$ source venv/bin/activate
```
If you are a Windows platform, you would activate the virtualenv like this:
```
% venv\Scripts\activate.bat
```
Once the virtualenv is activated, you can install the required dependencies.
```
$ pip install -r requirements.txt
```

Now let run the server locally
```
$ python manage.py migrate
$ python manage.py runserver
```
then go to http://127.0.0.1:8000/ or you can use diff port for example with port 8080  
```
$ python manage.py runserver 8080
```
---
# Upgrade Django
```
$ python -m pip install -U Django
$ python -Wa manage.py test # run all tests
```

# Documentation

## admin
You can access admin panel via `http://127.0.0.1:8000/admin/` (the default username/password are `root:root`)
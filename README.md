run server
==========
```
$ python3 -m venv venv
# venv\Scripts\activate  
$ python manage.py runserver # then go to http://127.0.0.1:8000/ or you can use diff port (python manage.py runserver 8080)
```

upgrade Django
=============
```
$ python -m pip install -U Django

# then test it
$ python -Wa manage.py test
```
* Create the project in terminal:
```
  django-admin startproject airline
  cd airline/
  python manage.py startapp flights
```
* Add the new app name `flights` to `INSTALLED_APP` in settings.py.
* Add a class `Flight` to define database columns.
### To affect the database
1. `python manage.py makemigrations` after models.py ready
2. Apply migration by ```python manage.py migrate``` 
3. Enter python shell by ```python manage.py shell```

* Include `flights.urls` in urls.py
* Create filghts/urls.py

### Add data into table
* Use object defined from `models.py` to add `Flight` and `Airport` inside shell
* Create `templates/flights/*.html` to design the web page.
* Launch the server from ```python manage.py runserver``` and type `localhost:8000/flights` in the browser

### Manipulate database from admin
*　`python manage.py createsuperuser`



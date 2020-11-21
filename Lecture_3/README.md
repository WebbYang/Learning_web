### HTTP Status Code
| Status Code | Description |
|:-----:|:-----:|
| 200 |  OK |
| 301 |  Moved Permanently |
| 403 |  Forbidden |
| 404 |  Not Found |
| 500 |  Internal Server Error |

### Django steps
* Install: `pip3 install Django`
* Create project: `django-admin startproject lecture3`
#### Hello
* Create app hello: `python manage.py startapp hello`
* Add `hello` in `INSTALLED_APPS` of `lecture3/settings.py` 
* Define function `index` in `hello/views.py`
* Create `hello/urls.py` and add path to urlpatterns 
* Include `hello/urls` route in `lecture3/urls.py`
* Check current result by: `python manage.py runserver` 
* Add new function `greet` with argument `name` in `hello/views.py` and add path to `hello/urls.py`
* Test with `localhost:8000/hello/webb`
* Modify index function to render `index.html` in `hello/views.py`
* Create `templates/hello/index.html` and `templates/hello/greet.html`.
* 

#### Newyear
* Create app newyear:`python manage.py startapp newyear`
* Add `newyear` `INSTALLED_APPS` of `lecture3/settings.py`
* Create `newyear/urls.py` and add path to urlpatterns 
* Include `newyear/urls` route in `lecture3/urls.py`
* Add variable in `index.html` by {% VARIABLE %}
* 

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
* Create app hello: `python manage.py startapp hello`
* Add `hello` in `INSTALLED_APPS` of `lecture3/settings.py` 
* Define function `index` in `hello/views.py`
* Create `hello/urls.py` and add path to urlpatterns 
* Include `hello/urls` route in `lecture3/urls.py`
* Check current result by: `python manage.py runserver` 
* Add new function `who` in `hello/views.py` and add path to `hello/urls.py`
* Test with `localhost:8000/hello/webb`

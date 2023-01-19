# About this Project:

Hi, this is an **online shopping system** project with Python & Django Framework & REST API


The repository is a start point for most of my professional projects; for this, I'm using as a part of my portfolio, feel free to use wherever you want. I'll be happy if you provide any feedback or code improvements or suggestions.

Connect with me at:

 [![](https://camo.githubusercontent.com/a493f6833f99fb3c85788d6d9305e6b7a42b838e5ee5d138fd9a8214a7e77472/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333030373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/sajjad-kashi-6097a3248/)

📫  How to reach me:  [sajjad.kashi2012@gmail.com](mailto:sajjad.kashi2012@gmail.com)
# Demo

[![demo](https://iili.io/HcdVJFs.gif)](https://iili.io/HcdVJFs.gif)

^ sorry about the bad quality, size restrictions :(

# Tools:

1.  Back-End: Python, Django, REST API
2.  Data Base: PostgreSQL
3.  Front-End: HTML5, CSS3, JavaScript, Bootstrap4, jQuery, AJAX

# Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder  `env`  in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with
```
pip install -r requirements.txt
```

Now you can run the project with this command
```
python manage.py runserver
```

**Note**  if you want payments or email  or sms   to work you will need to enter your own Stripe API keys into the  `.env`  file in the settings files.
# Features:

-   Login is done by sending SMS
-   "Cart" & "Contact Me" & "Profile" Pages are Single Page Application
-   Set Cookie to Add Product to Cart without Logging in
-   The shopping cart is stored to process its data and provide better offers to the customer.
-   All pages are responsive and suitable for mobile

# Testing

### [](https://github.com/leanerr/django_ecommerce#run-tests)Run tests:
```
python manage.py test
```
```

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

### [](https://github.com/leanerr/django_ecommerce#run-tests-with-coverage)Run tests with coverage:
```
pip install coverage
coverage run --source='.' manage.py test
```

### [](https://github.com/leanerr/django_ecommerce#check-coverage-report)Check coverage report:
```
coverage report
```
```

Name                                Stmts   Miss  Cover
-------------------------------------------------------
manage.py                              13      6    54%
mysite/__init__.py                      0      0   100%
mysite/settings.py                     18      0   100%
mysite/urls.py                          3      0   100%
mysite/wsgi.py                          4      4     0%
polls/__init__.py                       0      0   100%
polls/admin.py                          4      0   100%
polls/apps.py                           4      0   100%
polls/migrations/0001_initial.py        7      0   100%
polls/migrations/__init__.py            0      0   100%
polls/models.py                        20      1    95%
polls/templates/__init__.py             0      0   100%
polls/templates/polls/__init__.py       0      0   100%
polls/tests.py                         57      0   100%
polls/urls.py                           4      0   100%
polls/views.py                         28      8    71%
-------------------------------------------------------
TOTAL                                 162     19    88%
```


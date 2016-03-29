# The World Countries

API and web page made according to [this](http://cs629329.vk.me/v629329938/32a75/UpHITWBTRaU.jpg) "product requirements document".

Features:

1. Web-service can return following queries in format JSON/XML (use `format` GET parameter e.g. `/api/countries/1/?format=json`):
    1. World countries list (name, population) - `/api/countries/`
    2. Specific country details by it's id - `/api/countries/1`
    3. Top-5 most populated countries - `/api/countries/?page_size=5&ordering=-population`
2. Web-page that illustrates all queries from 1 paragraph - index page `/`

Also added admin interface (`/admin`) for convenient moderation.


## Prerequisites

* [Python 3](https://www.python.org/downloads/release/python-351/)
* [NPM](https://nodejs.org/en/)


## Installation

Be sure that Python and NodeJS directories in your system PATH variable.

1. Clone this repository
2. Open command line
3. Go to project root `cd path/to/project`
4. Install python libraries `pip install -r requirements.txt`
5. Create database `python manage.py migrate`
6. Install bower globally `npm install bower -g`
7. Install bower dependencies `python manage.py bower_install`
8. Copy staticfiles `python manage.py collectstatic`


## Fixtures

Load test data to database with commands:

```
python manage.py collectlanguages
python manage.py collectcountries
```

## Running

```
python manage.py runserver
```


## License

MIT
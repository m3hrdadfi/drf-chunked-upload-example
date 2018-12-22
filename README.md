# drf-chunked-upload example

[![Python Version](https://img.shields.io/badge/python-3.5-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Framework Version](https://img.shields.io/badge/djangorestframework-3.9-brightgreen.svg)](https://www.django-rest-framework.org/)

This is a Django demo project of the drf-chunked-upload module.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/m3hrdadfi/drf-chunked-upload-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a user (superuser):

```bash
python manage.py createsuperuser
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at **127.0.0.1:8000**.


## Support
If you find any bug or you want to propose a new feature, please use the [issues tracker](https://github.com/m3hrdadfi/drf-chunked-upload/issues). I'll be happy to help you! :-)

## License

The source code is released under the [MIT License](https://github.com/m3hrdadfi/drf-chunked-upload-example/blob/master/LICENSE).

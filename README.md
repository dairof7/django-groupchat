# GroupChat

Basic group chat using Django

## Beginning 🚀

_Clone this repository using the following command._

```
git clone https://github.com/untalsebastianb/bomberbot_project.git
```

### Prerequisites 📋

_Needed Technologies_

* Django==3.1.3
* django-cors-headers==3.5.0
* djangorestframework==3.12.2
* Pillow==8.0.1
* psycopg2==2.8.6

#### _Backend_
_Using the [requirements.txt](https://github.com/untalsebastianb/bomberbot_project/blob/master/requeriments.txt) install the prerequisites needed for backend on the environ_
```
pip3 install -r requirements.txt
```
#### _BaseData - Postgres_

You need to install Postgres (tested on version 10.14)
```
sudo apt-get install postgresql 
```
About Postgres Setting:
* 'ENGINE': 'django.db.backends.postgresql_psycopg2',
* 'NAME': 'chatdb',
* 'USER': 'solid',
* 'PASSWORD': '1122',
* 'HOST': 'localhost',
* 'PORT': '5432',

### Instalación 🔧

_To run the development server you must follow the following steps:_

_1. Make sure to make the migrations of the database using the following commands:_

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
_2. You can create a Superuser to admin the database_
```
python3 manage.py createsuperuser
```
_3. Access the django admin with_
```
http://127.0.0.1:8000/admin
```

_4. Enter the URL to access the login in the development environment._

```
http://127.0.0.1:8000/login
```

## Api URLs⚙️

### List all messages on database with pagination 
* message-list/
### List all messages of one user
* user-message-list/<kword>
### List all user on database
* user-list/


## Building tools 🛠️

<p align=“center”> <a href="https://www.w3schools.com/css/" target="_blank"> 
<img src="https://devicons.github.io/devicon/devicon.git/icons/css3/css3-original-wordmark.svg" alt="css3" width="60" height="60"/> 
</a> <a href="https://www.djangoproject.com/" target="_blank"> <img src="https://devicons.github.io/devicon/devicon.git/icons/django/django-original.svg" alt="django" width="60" height="60"/> </a> 
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://devicons.github.io/devicon/devicon.git/icons/html5/html5-original-wordmark.svg" alt="html5" width="60" height="60"/> </a> 
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://devicons.github.io/devicon/devicon.git/icons/javascript/javascript-original.svg" alt="javascript" width="60" height="60"/> </a> 


## Version 📌

_Current version: 1.0_

_Future updates:_
* Use WebScokets with Channels framework for realtime chat
* Build a Front-End in React-js

## Authors ✒️

* **Dairo Facundo Duarte** - *Backend Developer* - [dairof7](https://github.com/dairof7)

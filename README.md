# Python-API-Notes
###### Date Written: 4th July 2023
This page serves as a note for my API development and the content of this page is based on my research. You may reach out to me regarding any incorrect or outdated information.


## Table of Content
|S/N     |Title                                                                              |
|--------|-----------------------------------------------------------------------------------|
|1       |[Type of APIs](#API-Comparison)                                                    |
|2       |[Setting up DJango](#Setup-Django)                                                 |
|2.1     |[Executing DJango](#13-run-django)                                                 |
|3       |[Changeing Database for DJango](#Changing-databases-for-django)                    |
|4       |[Setting up Flask](#setup-flask)                                                   |
|4.1     |[Executing Flask](#execute-the-flask-program)                                      |
|5       |[Postgresql Installation and Information](#postgresql)                             |
|5.1     |[Connecting Postgresql with DJango](#changing-databases-for-django)                |
|5.2     |[Connecting Postgresql with Flask](#installation-of-postgres-in-python)            |
|5.3     |[Postgresql Forget User ID and Password](#postgresql-forgot-id-and-password)       |
|5.4     |[Postgresql basic commands](#2-restart-postgresql)                                 |
|6       |[CrateDB Concept](#cratedb)                                                        |
|6.1     |[CrateDB Documentation](#crate-documentation)                                      |
|6.2     |[CrateDB Local Installation](#cratedb-installtion)                                 |
|6.2     |[Connecting to CrateDB using crate library](#connect-to-cratedb)

## API Comparison
There are 3 frequently used APIs are coded in python, mainly ```DJango```, ```Flask Framework```, and ```Fast API```.  
All framework have their pros and cons and there is no definite best API to use for your API development. It all comes down to the purpose of your APIs.  

**1) DJango**  
DJango is built with Object-Relational Mapping in mind where users could easily define objects for development. It has an Admin Panel where users can simulate the insertion and querying of data without having to script an API call or use any external application to interact with the API. Moreover, it is easier to organise files with DJango especially for projects that are fairly large as it segmentise the API program into smaller bits. On the side note, DJango also have built in security features such as SQL injection, cross-site scripting and cross-site request forgery attacks protection in place.  

However, the learning curve for new users using DJango could be rather steep.  

**2) Flask Framework**  
Flask is rather easier to use as compared to DJango as the learning curve of flask is not as steep as DJangfo. It is useful for fast deployment of small and medium sized project.  

**3) Fast API**  
Fast API is a rather new framework that supports the use of asynchronous programming. It is able to handle high volume of request with little overhead and it is also easy to learn and deploy.  

Since Fast API is rather new, the security of the framework maybe lacking.  

## Django Tutorial
Django is a web framework and it can be used to build APIs using python. There are other options to build API on such as Flask API and FastAPI. In this section, Django is used due to scalability.  
By default, Django works on sqlite. However, it can be changed to meet the needs of users.  

### Setup Django
#### 1.1) Install Django
```
python -m pip install django
```
#### 1.2) Create Django project
A folder (projectName) will be created after the command shown below is executed. The folder will consist of another (projectName) folder and a manage.py file.
```
django-admin startproject (projectName)
```

#### 1.3) Run Django
```
python manage.py runserver
```
#### 1.4) Create API app
There is a practice to create API folder seperately from Django project. Thus if the project do not require the creation of another folder, then this step can be skipped.
```
python manage.py startapp (folderName)
```
After the command above is executed, you will have a few an additional folder, (folderName) as compared to **1.2)**.

#### 1.5) Add directory of the newly created folder into the main Django project.
Modify the following section in ```(projectName)/settings.py```. If the project do not require the creation of another folder, this step can be skipped too.
```
INSTALLED_APPS = [
    '(projectName).apps.(ProjectName)Config,
    # Do not remove other installed configuration. Replace (projectName) with your own and note the caps for the parameter with config.
]
```
#### 1.6) Initialise database on Django
Django will use this database for all of its functionality.
```
python manage.py migrate
```
#### 1.7) Create a superuser account to be used for Django
The superuser account will be used to access all admin section of Django. The admin section will greatly help you in developing your API.
```
python manage.py createsuperuser
Username (leave blank to use 'sweea'): 
Email address:
Password: 
Password (again): 
Superuser created successfully.
```

### Django framework
#### admin.py
This file is required if you would like to manage your api using the django web UI. You can initialise your API with the following.
```sh
from django.contrib import admin
from .models import (YourAPIModel)

admin.site.register(**(YourAPIModel)**)
```
#### models.py
This file contains all models (Class/Entity) required for your API. You will declare your models here before importing to other files. In this case, I will be initialising the variable value to **VARCHAR** that have a byte size of 50 character. You can reference https://docs.djangoproject.com/en/4.2/topics/db/models/, for more details on django model.  
```sh
from django.db import models

class testApi(models.Model):
    value = models.CharField(max_length=60)

    def __str__(self):
        return self.value
``` 
You will have to run **migrations** everytime you update your models
```sh
python manage.py makemigrations
```
#### views.py
This file contain functions that will be executed when an API route is called.  
```sh
from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

async def testAPIViewSet(request):
    return JsonResponse({"Success": "API is online"})
```
#### urls.py
This file contains the initialisation for url routing of API to their individual **views**.  
```sh
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
    path('testapi/', views.testAPIViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
#### serializers.py
This file converts all of your models to be represented in JSON format.


#### References:
1) https://www.youtube.com/watch?v=i5JykvxUk_A&t=982s  
2) https://awstip.com/use-django-rest-framework-without-creating-a-model-bee57357b214  
3) https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c  


## Changing databases for django
Go to **settings.py** and modify the following section.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘<db_name>’,
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }
}
```
There are only 4 **ENGINE** types in django. https://docs.djangoproject.com/en/dev/ref/settings/#databases  
1) 'django.db.backends.postgresql'  
2) 'django.db.backends.mysql'  
3) 'django.db.backends.sqlite3'  
4) 'django.db.backends.oracle'  

#### migrate
Always run migrate if you have modified any databases.
```sh
python manage.py migrate
```
#### Reference:
https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django


## Django to retrieve a list of available locale
If you ever require to modify locale for your django, you can get the list of locale here.
https://database.guide/how-to-return-a-list-of-available-collations-in-postgresql/

## Setup Flask
### Install Flask
Start off flask API with the installation of **Flask library** and no external installation is required for flask API.
```sh
python -m pip install Flask
```

### Initialise Flask
Create a python file with the following lines. Ensure that you are using the correct interpreter.
```sh
from flask import Flask
app = Flask(__name__)

@app.route('/testAPI')
def testAPI():
    return {'Success': 'API is Online'}
```

### Execute the flask program.
```sh
python -m flask --app (Python File Name) run
```
After executing the above command, you will be able to observe the following message:
```
 * Serving Flask app 'TestFlask'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
After which you may verify if your API is working. In this case, access ```http://127.0.0.1:5000/testAPI``` in your browser.

## Postgresql
You may install postgresql and setup on your computer from https://www.postgresql.org/download/.  

After downloading, the default user is ```postgres```. You may access the postgresql database using the following command.  
```sh
psql -U postgres
```
Postgresql will be hosted on port ```5432`` by default.  

You will be prompt for password afterwards.
**Reference:**  
1) https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm  

### Installation of postgres in python
Install postgresql library for python.
```sh
python -m install psycopg2
```
#### Connect to postgresql
You can access to postgresql using the following few lines of code.
```sh
import psycopg2

conn_pgs = psycopg2.connect(
    host="<host_name>",
    database="<database_name>",
    user="postgres",
    password="<password>"
)

cur = conn.cursor()
cur.execute("Select * from TableName;")

// Close database
conn.commit()
cur.close()
conn.close
```

## Postgresql Forgot ID and PASSWORD
In the case where you have forgotten your postgresql password, you can change your password using the following method.

### 1) ph_hba.conf
Search for **ph_hba.conf** in, (**15** is the version of your postgres)
```
C:\Program Files\PostgreSQL\15\data\ph_hba.conf
``` 
and modify all **METHOD** from ```scram-sha-256``` to ```trust```. 

### 2) Restart postgresql
Run the following command to restart postgresql. (**15** is the version of your postgres)
```sh
pg_ctl -D "C:\Program Files\PostgreSQL\15\data" restart
```

### 3) Access postgresql and modify password
Access postgresql
```sh
psql -U postgres
```

After accessing postgresql, modify your password
```sh
ALTER USER postgres WITH PASSWORD 'new password';
```

**Reference:**  
https://www.postgresqltutorial.com/postgresql-administration/postgresql-reset-password/

## CrateDB
There are a few types of crate service:  
1) CrateDB Cloud: Crate is a remote database and thus you do not need to perform any installation.  
2) CrateDB On-Premises: https://crate.io/download/thank-you (Download Link)  

CrateDB allows your to partition your data using certain values of your selected columns. For instance, the use of  
1) **CLUSTERED BY** is used to organise data within a shard;  
2) **PARTITIONED BY** is used to determine which data is stored in a shard.  
However, as of 1/6/2023, the downside of using **clustered by** and **partitioned by** is that you cannot declare a **primary key**.  

A shard contains data of a table in rows and it may consist of storage size from 2GB to 30GB (recommended).  
**References:**  
1) https://crate.io/docs/crate/reference/en/5.3/general/ddl/partitioned-tables.html
2) https://community.crate.io/t/sharding-and-partitioning-guide-for-time-series-data/737

### Crate Documentation
https://crate.io/docs/crate/reference/en/5.3/  

### CrateDB Installtion
Install crate library for python.
```sh
python -m install crate
```
### Running CrateDB On-Premises:
```
cd (Location Stored)/crate-(version)/
```
```
./bin/crate
```
After the above it done, you can access your CrateDB UI through
```
http://127.0.0.1:4200/
```

### Connect to crateDB
You can access to cratedb using the following few lines of code. If you are using the default access, the username should be **admin**.
```sh
from crate import client

conn = client.connect("
    <CrateDB given URL>:<CrateDB given port>", 
    username="admin", 
    password="<PASSWORD>", 
    verify_ssl_cert=True)

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.cluster")
    result = cursor.fetchone()
    print(result)
```
Do remember that ```with``` will automatically close the database after exiting.  
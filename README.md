# linkwebscrapper
Project Setup

The app uses the following tools:
Django
django rest framework
sqlite
jquery
bootstrap
celery
rabbitmq

So, to run it you need to install everything in requirements.txt inside a virutalenv. Add a SECRET_KEY as an environment variable. 
There are two ways to use the scrapper. By default, when you add a webpage, it will create an async task that will trigger the ´scrap_website´
function. Also, you can scrapp all webpages marked as "in_progress" by using the command ´python manage.py scrap´.

Feel free to comment and ask any question. 

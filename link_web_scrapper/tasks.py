from __future__ import absolute_import, unicode_literals
from celery import Celery
from link_web_scrapper.services import scrap_website

app = Celery('linkwebscrapper')


@app.task
def async_scrapp(webpage):
    try:
        scrap_website(webpage)
    except Exception as e:
        print(f"Error scrapping {webpage.name}: {e}")
    return

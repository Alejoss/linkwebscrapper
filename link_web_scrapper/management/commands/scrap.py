

from django.core.management.base import BaseCommand
from link_web_scrapper.models import WebPage, ScrappedLink
from link_web_scrapper.services import scrap_website


class Command(BaseCommand):
    help = 'scrrrrraping!'

    def handle(self, *args, **options):
        for webpage in WebPage.objects.filter(state="in_progress"):
            scrap_website(webpage)

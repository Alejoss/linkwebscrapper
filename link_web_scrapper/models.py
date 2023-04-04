from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class WebPage(models.Model):
    STATE_CHOICES = [
        ('in_progress', 'In Progress'),
        ('canceled', 'Canceled'),
        ('scrapped', 'Scrapped')
    ]
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='in_progress')
    deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.link

    class Meta:
        ordering = ["created_at"]


class ScrappedLink(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE, related_name="scrapped_links")
    created_at = models.DateTimeField(auto_now_add=True)
    url_name = models.CharField(max_length=150, blank=True)
    link = models.URLField()

    @classmethod
    def validate_link(cls, url):
        validator = URLValidator()
        try:
            validator(url)
            return True
        except ValidationError as e:
            print(f"{e} - Invalid URL: {url}")
            return False

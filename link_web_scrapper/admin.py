from django.contrib import admin
from link_web_scrapper.models import WebPage, ScrappedLink


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'state', 'created_at', 'deleted')


class ScrappedLinkAdmin(admin.ModelAdmin):
    list_display = ('webpage', 'link', 'url_name', 'created_at')


admin.site.register(WebPage, WebPageAdmin)
admin.site.register(ScrappedLink, ScrappedLinkAdmin)

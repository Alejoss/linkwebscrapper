from rest_framework import serializers
from link_web_scrapper.models import WebPage, ScrappedLink


class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = ['id', 'name', 'link', 'created_at', 'state', 'deleted']


class ScrappedLinkSerializer(serializers.ModelSerializer):
    webpage = WebPageSerializer()

    class Meta:
        model = ScrappedLink
        fields = ('id', 'webpage', 'created_at', 'url_name', 'link')

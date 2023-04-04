from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from link_web_scrapper.models import WebPage, ScrappedLink
from link_web_scrapper.serializers import WebPageSerializer, ScrappedLinkSerializer
from link_web_scrapper.tasks import async_scrapp


def index(request):
    webpages = WebPage.objects.all()
    context = {
        'webpages': webpages
    }
    return render(request, 'index.html', context)


def webpage_links(request, webpage_id):

    webpage = get_object_or_404(WebPage, id=webpage_id)

    context = {
        'webpage': webpage
    }
    return render(request, 'webpage_links.html', context)


class WebPageIndexView(APIView):
    def get(self, request):
        webpages = WebPage.objects.all()
        serializer = WebPageSerializer(webpages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WebPageSerializer(data=request.data)
        if serializer.is_valid():
            webpage_instance = serializer.save()
            try:
                async_scrapp.delay(webpage_instance)  # Sends it to Celery
            except Exception as e:
                print(f"Async Scrapp Error: {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScrappedLinkPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class WebPageLinksView(ListAPIView):
    serializer_class = ScrappedLinkSerializer
    pagination_class = ScrappedLinkPagination

    def get_queryset(self):
        print(f"self.request.GET: {self.request.GET}")
        webpage_id = self.request.GET['webpage_id']
        return ScrappedLink.objects.filter(webpage__id=webpage_id).order_by('-created_at')

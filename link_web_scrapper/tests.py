from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from link_web_scrapper.models import WebPage
from link_web_scrapper.serializers import WebPageSerializer


class WebPageIndexViewTest(APITestCase):
    def test_create_webpage(self):
        url = reverse('webpage-list')
        data = {
            'link': 'https://www.example.com',
            'state': 'in_progress',
            'deleted': False,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WebPage.objects.count(), 1)
        self.assertEqual(WebPage.objects.get().link, 'https://www.example.com')
        self.assertEqual(WebPage.objects.get().state, 'in_progress')
        self.assertEqual(WebPage.objects.get().deleted, False)

    def test_get_webpage(self):
        webpage = WebPage.objects.create(
            link='https://www.example.com',
            state='in_progress',
            deleted=False
        )
        url = reverse('webpage-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = WebPageSerializer([webpage], many=True)
        self.assertEqual(response.data, serializer.data)

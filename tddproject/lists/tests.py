from django.urls import resolve
from .views import index_page
from django.test import TestCase
from django.http import HttpResponse
from .models import Item

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        item = Item()
        item.text = 'First item'
        item.save()

        item2 = Item()
        item2.text = 'Second item'
        item2.save()

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)
        savedItem = items[0]
        savedItem2 = items[1]
        self.assertEqual(savedItem.text, 'First item')
        self.assertEqual(savedItem2.text, 'Second item')

class IndexTest(TestCase):

    def test_index_usage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_saving_post_request(self):
        self.client.post('/', data={'item_text': 'New li'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'New li')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'New li'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


class ListsViewTest(TestCase):

    def test_showing_all_items(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')
        response = self.client.get('/lists/only-one')
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')
from django.urls import resolve
from .views import index_page
from django.test import TestCase
from django.http import HttpResponse
from .models import Item, List


class IndexTest(TestCase):

    def test_index_usage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


class NewListTest(TestCase):

    def test_saving_post_request(self):
        other_list = List.objects.create()
        current_list = List.objects.create()
        self.client.post('/lists/{current_list.id}/new_item', data={'item_text': 'New li'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'New li')
        self.assertEqual(new_item.list, current_list)

    def test_redirects_after_POST(self):
        other_list = List.objects.create()
        current_list = List.objects.create()
        response = self.client.post('/lists/{current_list.id}/new_item', data={'item_text': 'New li'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{current_list.id}/')


class ListsViewTest(TestCase):

    def test_checking_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_passes_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)


class ItemListModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        item = Item()
        item.text = 'First item'
        item.list = list_
        item.save()

        item2 = Item()
        item2.text = 'Second item'
        item2.list = list_
        item2.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)

        saved_item = items[0]
        saved_item2 = items[1]
        self.assertEqual(saved_item.text, 'First item')
        self.assertEqual(saved_item.list, list_)
        self.assertEqual(saved_item2.text, 'Second item')
        self.assertEqual(saved_item2.list, list_)







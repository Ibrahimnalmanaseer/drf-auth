from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
from django.contrib.auth import get_user_model
from .models import Book

from django.urls import reverse

class BookTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_thing = Book.objects.create(
            title="harry",
            author='rolling',
            user=testuser1,
            rate=4,
            desc="a drama novel ",
            type='drama'
        )
        test_thing.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_things_model(self):
        book= Book.objects.get(id=1)
        actual_owner = str(book.user)
        actual_name = str(book.title)
        actual_description = str(book.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "harry")
        self.assertEqual(
            actual_description, "a drama novel "
        )

    def test_get_book_list(self):
        url = reverse("books")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("books")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("book", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


        
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fizzbuzz.models import FizzBuzz

class CreateFizzBuzzTests(APITestCase):
    def test_create_fizzbuxx(self):
        url = "/fizzbuzz/"
        data = {"message": "test"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FizzBuzz.objects.count(), 1)
        self.assertEqual(FizzBuzz.objects.get().message, "test")

class GetFizzBuzzTests(APITestCase):
    def test_all_fizzbuzz(self):
        url = "/fizzbuzz/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_fizzbuzz(self):
        self.fizzbuzz = FizzBuzz.objects.create(message="test")
        url = "/fizzbuzz/1/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fizzbuzz_id'], 1)
from rest_framework import status
from django.shortcuts import reverse
from user.models import Profile
from rest_framework.test import APIClient, APITestCase


class TestCV(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def create_user(self, username, password):
        user = Profile.objects.create_user(
            username, password
        )
        context = {
            'user': user,
            'username': user.username,
            'password': password
        }
        return context

    def get_token(self, username, password):
        url = reverse('login')
        resp = self.client.post(
            url,
            {"username": username, "password": password}, HTTP_USER_AGENT='test_user', HHTP_REMOTE_ADDR='127.0.0.1',
            format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in resp.data)
        self.assertTrue("refresh" in resp.data)
        self.access = resp.data["access"]
        self.refresh = resp.data["refresh"]
        tokens = {'access': self.access, 'refresh': self.refresh}
        return tokens

    def test_add_skill(self):
        user = self.create_user('ali', '12345')
        tokens = self.get_token(user['username'], user['password'])
        token = f'Bearer {tokens["access"]}'
        url = reverse('add_skill')
        data = {'title': 'test_skill', 'level': 'basic'}
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_add_education(self):
        user = self.create_user('ali', '12345')
        tokens = self.get_token(user['username'], user['password'])
        token = f'Bearer {tokens["access"]}'
        url = reverse('add_education')
        data = {'title': 'test_education', 'university': 'sharif', 'start_date': '2020-10-10', 'end_date': '2023-10-10'}
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_add_certificate(self):
        user = self.create_user('ali', '12345')
        tokens = self.get_token(user['username'], user['password'])
        token = f'Bearer {tokens["access"]}'
        url = reverse('add_certificate')
        data = {'title': 'test_education', 'certified_body': 'sharif', 'duration': '1 month'}
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_add_language(self):
        user = self.create_user('ali', '12345')
        tokens = self.get_token(user['username'], user['password'])
        token = f'Bearer {tokens["access"]}'
        url = reverse('add_language')
        data = {'title': 'test_education', 'level': 'native'}
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_add_language_bad_request(self):
        user = self.create_user('ali', '12345')
        tokens = self.get_token(user['username'], user['password'])
        token = f'Bearer {tokens["access"]}'
        url = reverse('add_language')
        data = {'title': 'test_education', 'level': 'hgctuy'}
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return response.data

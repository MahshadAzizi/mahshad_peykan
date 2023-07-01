from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from user.models import Profile
from rest_framework import status


class TestUser(APITestCase):
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

    def get_token_ok(self, username, password):
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

    def test_get_token_not_exist(self):
        url = reverse('login')
        username = 'abcd'
        password = "123"
        resp = self.client.post(
            url,
            {"username": username, "password": password}, HTTP_USER_AGENT='test_user', HHTP_REMOTE_ADDR='127.0.0.1',
            format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_register(self):
        url = reverse('register')
        response = self.client.post(
            url, {'first_name': 'mahshad', 'last_name': 'azizi', 'username': 'mahshad',
                  'password': '12345678M', 'email_address': 'mahshad@example.com'}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_login(self):
        user = self.create_user('mahshad', '12345678M')
        url = reverse('login')
        response = self.client.post(
            url, {'username': user['username'], 'password': user['password']}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def test_logout(self):
        user = self.create_user('admin3', '1234')
        tokens = self.get_token_ok(user['username'], user['password'])
        url = reverse('logout')
        token = f'Bearer {tokens["access"]}'
        response = self.client.post(
            url, {'refresh': tokens["refresh"]}, HTTP_AUTHORIZATION=token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



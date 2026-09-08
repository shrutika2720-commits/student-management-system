from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    def test_signup_and_login(self):
        # Sign up a new user
        resp = self.client.post(reverse('accounts:signup'), data={
            'username': 'tester',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        # After signup we redirect to login
        self.assertEqual(resp.status_code, 302)
        # Login with new user
        login = self.client.login(username='tester', password='complexpassword123')
        self.assertTrue(login)

from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTest(TestCase):
    def test_create_user_with_email_succesful(self):
        email='test@mail.com'
        first_name = 'Eduardo'
        last_name = 'Altuzar'
        password='Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
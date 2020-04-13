from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'test@edigraphs.com'
        password = 'Testpass234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

        def test_new_user_email_normalized(self):
            """Test the email for a new user is normalized"""
            email = 'test@EDIGRAPHS.COM'
            user - get_user_model().objects.create_user(email, 'test234')

            self.assertEqual(User.email, email.lower())

        def test_new_user_invalid_email(self):
            """Test creating user with no email raises error"""
            with self.assertRaises(ValueError):
                get_user_model().objects.create_user(None, 'test234')

            def test_create_new_superuser(self):
                """Test creating a new superuser"""
                user = get_user_model().objects.create_superuser(
                    'test@edigraphs.com',
                    'test234'
                )

                self.assertTrue(User.is_superuser)
                self.assertTrue(User.is_staff)

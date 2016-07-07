from django.test import TestCase
from social_api import user_manager
from wheel.signatures import assertTrue
from .models import User

# Create your tests here.


class UserManagerTest(TestCase):
    def test_create_user(self):
        google_info = {
            'family_name': 'Levi',
            'given_name': 'Eldad',
            'email': 'elda@k.com',
            'id':'2',
        }

        u, created = user_manager.get_or_create(google_info)
        self.assertTrue(created)
        self.assertTrue(u.id == User.objects.get(pk=u.pk).id)

    def test_duplication(self):
        google_info = {
            'family_name': 'Assayag',
            'given_name': 'Haim',
            'email': 'haim@k.com',
            'id': '34',
        }

        u, created = user_manager.get_or_create(google_info)
        self.assertTrue(created)
        self.assertTrue(u.id == User.objects.get(pk=u.pk).id)

        # test duplication
        dup, created = user_manager.get_or_create(google_info)
        self.assertFalse(created)
        self.assertTrue(dup.first_name == u.first_name)
        self.assertTrue(User.objects.filter(token=google_info['id'] + google_info['email']).count() == 1)


    def test_db(self):
        google_info1 = {
            'family_name': 'Levi',
            'given_name': 'Eldad',
            'email': 'elda@k.com',
            'id': '2',

        }
        google_info2 = {
            'family_name': 'Assayag',
            'given_name': 'Haim',
            'email': 'haim@k.com',
            'id': '34',
        }

        user_manager.get_or_create(google_info1)
        user_manager.get_or_create(google_info2)
        user_manager.get_or_create(google_info1)
        user_manager.get_or_create(google_info1)
        user_manager.get_or_create(google_info2)
        user_manager.get_or_create(google_info1)

        self.assertTrue(User.objects.all().count() == 2)
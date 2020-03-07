from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from features.models import Feature


class TestFeatureViews(TestCase):
    """
    List of tests to be run against
    the views for the features app
    """
    c = Client()

    def setUp(self):
        """
        Set up method for unit testing the features app.
        Instance of User and Feature created
        here and called in tests.
        """
        user = User.objects.create_user(
            'test_user',
            'test_user@mail.com',
            'example'
        )

        user.save()
        feature = Feature.objects.create(
            name='New feature',
            # details='New feature detail',
            requested_by=user)
        feature.save()
        logged_in = self.c.login(username='testing', password='test')

    def test_get_features(self):
        response = self.c.get('/features/get_features/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'features.html')


    def test_create_feature_page(self):
        feature = Feature.objects.get(id=1)
        response = self.c.get('/features/create_feature/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(feature, Feature))
        self.assertTemplateUsed(response, 'create_feature.html')

    def test_POST_create_feature_page(self):
        response = self.client.post("/features/create_feature/", {
            'name': 'Requesting a feature',
            'details': 'A new feature'
            }
        )
        self.assertEqual(response.status_code, 302)

    
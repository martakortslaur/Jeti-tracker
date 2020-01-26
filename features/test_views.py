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
        Instance of User, Feature and Comment created
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
            details='Yet another one',
            requested_by=user)
        feature.save()
        logged_in = self.c.login(username='test_user', password='example')

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
            'name': 'A new feature',
            'details': 'This would be a good feature'
            }
        )
        self.assertEqual(response.status_code, 302)

    
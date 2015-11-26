from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db.models import QuerySet
from django.test import TestCase
from place.models import Country


class CountryViewCase(TestCase):
    @classmethod
    def setUpClass(cls):
        Country.objects.create(pk=1, name='Ukraine')
        Country.objects.create(pk=2, name='Spain')
        get_user_model().objects.create_superuser(username='admin', email='admin@site.com', password='123456')
        super(CountryViewCase, cls).setUpClass()

    def test_view_list(self):
        r = self.client.get(reverse('countries'))
        self.assertEqual(r.status_code, 200)
        self.assertIn('object_list', r.context)
        self.assertIsInstance(r.context['object_list'], QuerySet)
        self.assertEqual(r.context['object_list'].model, Country)

    def test_view_detail_200(self):
        r = self.client.get(reverse('country', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Ukraine')
        k = self.client.get(reverse('country', kwargs={'pk': 2}))
        self.assertContains(k, 'Spain')
        self.assertIsInstance(r.context['object'], Country)

    def test_not_contains(self):
        r = self.client.get(reverse('country', kwargs={'pk': 2}))
        self.assertEqual(r.status_code, 200)
        self.assertNotContains(r, 'Ukraine')

    def test_view_empty_page_detail_404(self):
        r = self.client.get(reverse('country', kwargs={'pk': 4}))
        self.assertEqual(r.status_code, 404)

    def test_view_edit_403(self):
        r = self.client.get(reverse('country_edit', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 403)

    def test_view_edit_anonymous_user_403(self):
        r = self.client.get(reverse('country_edit', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 403)

    def test_view_edit(self):
        login_ok = self.client.login(username='admin', password='123456')
        r = self.client.get(reverse('country_edit', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        r = self.client.post(reverse('country_edit', kwargs={'pk': 1}), {
            'name': 'Ukraine 2'
        })
        self.assertRedirects(r, reverse('country', kwargs={'pk': 1}))
        self.assertEqual(Country.objects.get(pk=1).name, 'Ukraine 2')
        k = self.client.get(reverse('country_edit', kwargs={'pk': 1}))
        self.assertContains(k, 'Ukraine 2')
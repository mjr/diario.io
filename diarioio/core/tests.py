from django.test import TestCase, Client
from django.urls import reverse
from .forms import EntradaForm


class EntradaGetTest(TestCase):
    def setUp(self):
        client = Client()
        self.resp = client.get(reverse('home'))

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_html(self):
        self.assertContains(self.resp, '<form', 1)
        self.assertContains(self.resp, '<input', 3)
        self.assertContains(self.resp, '<textarea', 2)
        self.assertContains(self.resp, 'type="submit"', 1)


class EntradaPostTest(TestCase):
    def setUp(self):
        client = Client()
        entrada_form = EntradaForm()
        self.resp = client.post(reverse('home'), {'entrada_form': entrada_form})

    def test_entrada_form(self):
        entrada_form = EntradaForm()
        entrada_form_req = EntradaForm(self.resp.POST)
        self.assertIsInstance(self.resp, entrada_form, entrada_form_req)

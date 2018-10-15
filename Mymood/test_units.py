# content of test_sample.py
from Mymood.biz import process_happiness, process_teams, process_members, process_events
from django.test import TestCase
from models_app.models import *
from django.test import TestCase
from django.test import Client

class MyClassTestCase(TestCase):

    def setUp(self):
        # Setup run before every test method.
        pass

    def test_get_webhook(self):
        self.client.get('/get_webhook')

    def tearDown(self):
        # Clean up run after every test method.
        pass




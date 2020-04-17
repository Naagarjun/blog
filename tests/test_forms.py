import unittest
from django.contrib.auth.models import User
from accounts.forms import UpdateDetails, UserRegisterForm
from django.test import TestCase

class TestAccountsForms(TestCase):

    def test_acccounts_registration_forms(self):
        details= User.objects.create(username='arjun')
        data= {'username':details.username}
        form= UpdateDetails(data=data)
        self.assertTrue(form.is_valid)

    def test_user_registration_form(self):
        details=User.objects.create(username='arjun', email='arjun@mail.com')
        data={'username':details.username, 'email':details.email}
        form = UserRegisterForm(data=data)
        self.assertTrue(form.is_valid)
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import VERSION as DJANGO_VERSION
from django.core.exceptions import ValidationError
from django.test import TestCase
from dns.exception import DNSException
from mock import patch
from test_app.forms import EmailForm
from unittest import skipIf


class TestEmailFormField(TestCase):

    """Tests for the :py:class:`thecut.emailfield.models.EmailField`
    model field."""

    @patch('dns.resolver.query')
    def test_rejects_domain_without_mx_record(self, fake_query):
        """Reject email address for a domain without an MX record."""
        fake_query.side_effect = DNSException()
        form = EmailForm(data={'email': 'development@thecut.net.au'})
        self.assertFalse(form.is_valid())
        # Enure dns.resolver.query() was actually called.
        fake_query.assert_called_once_with('thecut.net.au', 'MX')

    @patch('dns.resolver.query')
    def test_accepts_domain_with_mx_record(self, fake_query):
        """Accept email address for a domain with an MX record."""
        form = EmailForm(data={'email': 'development@thecut.net.au'})
        self.assertTrue(form.is_valid())
        # Enure dns.resolver.query() was actually called.
        fake_query.assert_called_once_with('thecut.net.au', 'MX')

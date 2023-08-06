# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator as DjangoEmailValidator
from django.utils.encoding import force_text
from dns import resolver
from dns.exception import DNSException


class EmailValidator(DjangoEmailValidator):
    """Extended EmailValidator which checks for MX records on the domain."""

    def __call__(self, value, *args, **kwargs):
        super(EmailValidator, self).__call__(value, *args, **kwargs)

        value = force_text(value)

        domain = value.split('@')[1]
        try:
            resolver.query(domain, 'MX')
        except DNSException:
            raise ValidationError('Enter a valid email address domain.',
                                  code=self.code)


validate_email = EmailValidator()

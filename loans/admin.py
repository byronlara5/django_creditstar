# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from loans.models import Loan, Message


# Register your models here.

admin.site.register(Loan)
admin.site.register(Message)
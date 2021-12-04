# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Invoice

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = ('id', 'date_pay', 'total')
    list_select_related = ('client',)
    raw_id_fields = ('client',)
    search_fields = ('client',)

admin.site.register(Invoice, InvoiceAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Invoice(models.Model):
    PENDING = 0
    PAID = 1
    PARTIAL = 2
    CANCELLED = 3
    REVISION = 4
    INVOICE_STATUS = (
        (PENDING, 'Pending payment'),
        (PAID, 'Paid'),
        (PARTIAL, 'Partial'),
        (CANCELLED, 'Cancelled'),
        (REVISION, 'In review'),
    )

    date_pay = models.DateTimeField()
    state = models.PositiveSmallIntegerField(choices=INVOICE_STATUS, default=PENDING, db_index=True)

    total = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, verbose_name="Payment Reference", blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cliente_factura", null=True,
                                verbose_name="Client")

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'{0}'.format(self.id)
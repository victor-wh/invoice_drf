# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Invoice

import datetime

# Create your views here.

"""Como seria la api sin django rest Framework"""
def list_invoices(request):
    """List of Invoice"""
    invoices = Invoice.objects.all()
    data = []

    for invoice in invoices:
        data.append({
            'id': invoice.id,
            'client': str(invoice.client),
            'total': invoice.total,
            'status': invoice.state,
        })
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def list_invoices_drf(request):
    """
        ENDPOINT: Consultar la informacion de las facturas mediante DRF
        usar: http GET localhost:8000/invoices-drf/ -b
    """
    data = []
    invoices = Invoice.objects.select_related('client').all()
    for invoice in invoices:
        data.append({
            'id': invoice.id,
            'client': str(invoice.client),
            'total': invoice.total,
            'status': invoice.state,
        })
    
    return Response(data)


@csrf_exempt
@api_view(['POST'])
def create_invoice(request):
    """
        ENDPOINT: Crear nueva factura con DRF
        usar: http POST localhost:8000/invoices/create/ total=40 reference=23423 client=1 -v
    """
    today = datetime.datetime.now()
    date_pay = today
    # Datos obtenidos del request
    total = request.data['total']
    reference = request.data['reference']
    client = request.data['client']
    # Se crea la factura
    invoice = Invoice.objects.create(date_pay=date_pay, total=float(total), reference=reference, client_id=client)
    data = {
        'id': invoice.id,
        'client': str(invoice.client),
        'total': invoice.total,
        'status': invoice.state,
    }

    return Response({ "message": "Factura: " + str(invoice.id) + " Creada", "data": data})


@csrf_exempt
@api_view(['POST'])
def update_invoice(request):
    """
        ENDPOINT: Editar factura con DRF
        usar: http POST localhost:8000/invoices/update/ id=1 total=100 reference=23423 client=1 -v
    """

    # Datos obtenidos del request
    id = int(request.data['id'])
    total = request.data['total']
    reference = request.data['reference']
    client = request.data['client']

    invoices = Invoice.objects.filter(id=id)
    invoices.update(total=float(total), reference=reference, client_id=client)

    data = []
    for invoice in invoices:
        data = {
            'id': invoice.id,
            'client': str(invoice.client),
            'total': invoice.total,
            'status': invoice.state,
        }

    return Response({ "message": "Factura: " + str(id) + " Editada", "data": data})


@csrf_exempt
@api_view(['POST'])
def delete_invoice(request):
    """
        ENDPOINT: Editar factura con DRF
        usar: http POST localhost:8000/invoices/delete/ id=9 -v
    """

    # Datos obtenidos del request
    id = int(request.data['id'])

    invoices = Invoice.objects.filter(id=id)

    data = []
    for invoice in invoices:
        data = {
            'id': invoice.id,
            'client': str(invoice.client),
            'total': invoice.total,
            'status': invoice.state,
        }
    
    invoices.delete()

    return Response({ "message": "Factura: " + str(id) + " Eliminada", "data": data})

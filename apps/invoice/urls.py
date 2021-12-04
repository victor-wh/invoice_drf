from django.conf.urls import url, include
from views import list_invoices, list_invoices_drf, create_invoice, update_invoice, delete_invoice

urlpatterns = [
   url(r'^invoices/$',list_invoices,name="invoices"),
   url(r'^invoices-drf/$',list_invoices_drf,name="invoices_drf"),
   url(r'^invoices/create/$',create_invoice,name="invoices_create"),
   url(r'^invoices/update/$',update_invoice,name="invoices_update"),
   url(r'^invoices/delete/$',delete_invoice,name="invoices_delete"),
]

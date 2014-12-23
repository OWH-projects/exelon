from models import *
from django.shortcuts import *
from django.db.models import *
from exelon.models import *
from django.http import HttpResponse

def Main(request):
    invoices = Invoice.objects.all().order_by('invoicedate')
    sum = invoices.aggregate(Sum('amount'))['amount__sum']
    average = invoices.aggregate(Avg('amount'))['amount__avg']
    median = Invoice.objects.all().order_by('amount')[int(round(invoices.count() / 2))]
    dictionaries = { 'invoices': invoices, 'sum':sum, 'average':average, 'median':median,  }
    return render_to_response('exelon/main.html', dictionaries)
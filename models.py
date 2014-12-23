from django.db import models
#from django.db.models import *
import datetime

class Invoice(models.Model):
    invoicedate = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=False)
    url = models.CharField(max_length=300, null=False, blank=False)
    #str = str(invoicedate)

    class Meta:
        db_table = u'exelon'

    def __unicode__(self):
        return str(self.invoicedate)
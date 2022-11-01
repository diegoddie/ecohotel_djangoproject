from django.db import models
from django.utils import timezone 
from .utils import sendTransactionAndGetTxId
import hashlib

# Create your models here.

class PhotovoltaicPanel(models.Model):
    produced_energy = models.IntegerField(null=True)
    consumed_energy = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    hash = models.CharField(max_length=32, default=None, null=True, blank=True)
    txId = models.CharField(max_length=66, default=None, null=True, blank=True)

    def __str__ (self):
        return self.date.strftime("%Y-%m-%d")

    def writeOnChain(self):
        self.hash = hashlib.sha256(str(self.produced_energy).encode("utf-8")).hexdigest()+hashlib.sha256(str(self.consumed_energy).encode("utf-8")).hexdigest()
        self.txId = sendTransactionAndGetTxId(self.hash)
        self.save()


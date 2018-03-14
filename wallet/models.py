from django.db import models

# Create your models here.

class UserWallet(models.Model):
    wallet_address = models.CharField(max_length=100, db_index=True, unique=True)
    reference = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
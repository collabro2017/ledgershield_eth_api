from django.db import models

# Create your models here.

class NodeConfig(models.Model):

    master_wallet_address = models.TextField()
    master_wallet_password = models.CharField(max_length=100)
    node_url = models.URLField()
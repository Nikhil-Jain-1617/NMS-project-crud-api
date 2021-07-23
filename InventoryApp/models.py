from django.db import models

class ServerInventory(models.Model):
    ip_address = models.CharField(max_length=20)
    os_type = models.CharField(max_length=30)
    server_type = models.CharField(max_length=30)

    def __str__(self):
        return self.ip_address
# Create your models here.

from django.db import models

# Create your models here.
class Domain(models.Model):
    # DOMAIN NAME
    domain_Name = models.CharField(max_length=30)
    # LINK TO REGISTRAR
    domain_Registrar = models.CharField(max_length=30)
    # NAME OF PERSON WHO OWNS IT
    domain_Owner = models.CharField(max_length=30)
    #DATE OF EXPIRY
    domain_Expiration = models.DateField()
    #PRICE TO RENEW
    domain_Renew_Fee = models.DecimalField(max_digits=6, decimal_places=2)
    # YEARLY OR MONHTLY 
    domain_Renew_TimePeriod = models.CharField(max_length=10)

    domain_Link = models.CharField(max_length=30)
    # Link for Registrar
    domain_Registrar_Link = models.CharField(max_length=30)
class Contact(models.Model):
    email = models.CharField(max_length=30)

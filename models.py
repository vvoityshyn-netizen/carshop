from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    car = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Purchase(models.Model):
    car = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    from django.db import models

class Payment(models.Model):
    card_last4 = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"**** {self.card_last4}"
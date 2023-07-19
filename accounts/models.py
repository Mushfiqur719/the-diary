from django.db import models

# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('Income','Income'),
        ('Expense','Expense'),
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    party_name = models.CharField(max_length=50,blank=True, null=True)
    details = models.TextField(blank=True,null=True)
    amount = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Date: {self.date}, Client: {self.party_name}"
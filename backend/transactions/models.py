from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount}"
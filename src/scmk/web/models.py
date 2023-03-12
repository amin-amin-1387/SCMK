from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __unicode__(self):
        return f"{self.date}-{self.user}-{self.amount}"


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __unicode__(self):
        return f"{self.date}-{self.user}-{self.amount}"
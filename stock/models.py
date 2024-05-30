from django.db import models

# Create your models here.

from django.db import models

class Stock(models.Model):
    
    StockID = models.CharField(max_length=20, unique=True)
    StockName = models.CharField(max_length=100)
    Exchange = models.CharField(max_length=50)
    Category_code = models.CharField(max_length=20)
    Category = models.CharField(max_length=50)
    Reference = models.CharField(max_length=100)
    ShareCapital = models.DecimalField(max_digits=20, decimal_places=2)
    Total_Shares = models.BigIntegerField()
    MarketCapital = models.DecimalField(max_digits=20, decimal_places=2)
    Chairman = models.CharField(max_length=20)
    DayTrade = models.BooleanField()

    def __str__(self):
        return f"{self.StockName} ({self.StockID})"
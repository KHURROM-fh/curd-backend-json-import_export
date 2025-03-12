from django.db import models


"""TRADECODE_LIST= [
    ('',''),
] """
class StockData(models.Model):
    date = models.CharField(max_length=50)
    tradecode = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.tradecode} - {self.date}"
    class Meta:
        verbose_name_plural= "Stork Data"
        ordering = ['date']
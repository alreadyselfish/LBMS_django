from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=False, max_length=500)
    number_of_pages = models.IntegerField(null=True)
    price = models.IntegerField(default=199)

    @property
    def our_price(self):
        if not self.number_of_pages:
            return int(self.price*0.88)
        return int(min(self.number_of_pages*0.5, self.price*0.9))
    
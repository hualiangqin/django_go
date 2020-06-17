from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField()

    def get_absolute_url(self):
        # need to include the app name before the name of the path
        return reverse("products:product_detail", kwargs={"id": self.id}) #f"/products/{self.id}/"

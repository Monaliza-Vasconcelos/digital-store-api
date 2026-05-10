from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    reference = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.URLField()

    def __str__(self):
        return f"Imagem de {self.product.name}"

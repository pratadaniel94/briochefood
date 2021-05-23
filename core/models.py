from django.db import models


class Seller(models.Model):
    cities = (
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro')
    )
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=5, choices=cities, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField(max_length=1000)
    # activate = models.BooleanField(default=True)
    # provider = models.OneToOneField(Provider, )

    def __str__(self):
        return self.title

class Seller_Product(models.Model):
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=False)

    def __str__(self):
        return f"Seller: {self.id_seller} Product: {self.id_product}"

    class Meta:
        unique_together = ('id_seller', 'id_product',)


# class Order(models.Model):
#     provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_name='requests')
#     products = models.ManyToManyField(Product)

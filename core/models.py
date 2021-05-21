from django.db import models

class Provider(models.Model):
    cities = (
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro')
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=5, choices=cities, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    activate = models.BooleanField(default=True)
    # provider = models.OneToOneField(Provider, )

    def __str__(self):
        return self.title

# class Order(models.Model):
#     provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_name='requests')
#     products = models.ManyToManyField(Product)

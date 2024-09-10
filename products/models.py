from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)  # type: ignore
    img = models.ImageField(upload_to='img')  # type: ignore
    base_price = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)

    def __str__(self):
        return self.name
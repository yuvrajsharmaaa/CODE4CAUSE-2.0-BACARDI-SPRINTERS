from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

class PersonalityTest(models.Model):
    personality_type = models.CharField(max_length=10)
    recommended_color = models.CharField(max_length=50, blank=True, null=True)

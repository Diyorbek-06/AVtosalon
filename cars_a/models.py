from django.db import models

# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=123)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=27)
    miliage = models.PositiveIntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=10)
    desciptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        ordering = ['update_at']
        verbose_name = 'Cars'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
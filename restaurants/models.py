from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
    	return self.name

class Item(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.name
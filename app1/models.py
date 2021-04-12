from django.db import models
from django.conf import settings
from users.models import CustomUser

# Create your models here.
DEFAULT_TYPE = 1
TYPE_CHOICES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna'),

)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=DEFAULT_TYPE)
    categories = models.ManyToManyField(Category, related_name='institution')


class Donation(models.Model):
    # liczba worków
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donation')
    institution = models.ForeignKey(Institution, related_name='donation', on_delete=models.CASCADE)

    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    city = models.TextField()
    zip_code = models.TextField()

    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#datefield
    pick_up_date = models.DateField()
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#timefield
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    # user = models.ForeignKey(User, related_name='donation', on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='donation')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

from django.db import models
from django.conf import settings

from django.contrib import admin

from accounts.models import User

# Create your models here.
DEFAULT_TYPE = 1
TYPE_CHOICES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna'),

)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Category, CategoryAdmin)
class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=DEFAULT_TYPE)
    categories = models.ManyToManyField(Category, related_name='institution')

    def __str__(self):
        return self.name
    
#     https://docs.djangoproject.com/pl/3.2/intro/tutorial07/#customize-the-admin-form
class InstitutionAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Institution, InstitutionAdmin)

class Donation(models.Model):
    # liczba worków
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donation')
    # instytucje
    institution = models.ForeignKey(Institution, related_name='donation', on_delete=models.CASCADE)
    # (ulica plus numer dom
    address = models.CharField(max_length=64)
    # numer telefonu
    phone_number = models.CharField(max_length=16)
    city = models.TextField()
    zip_code = models.TextField()

    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#datefield
    pick_up_date = models.DateField()
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#timefield
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True, null=True)
    # user = models.ForeignKey(User, related_name='donation', on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

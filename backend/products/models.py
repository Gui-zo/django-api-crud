import random
from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL  # auth.User

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        queryset = self.is_public().filter(lookup) # makes sure that the data you are searching is public
        if user is not None:
            queryset2 = self.filter(user=user).filter(lookup)
            queryset = (queryset | queryset2).distinct()
        return queryset


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs): # Overriding the default method
        return ProductQuerySet(self.model, using=self._db) # This is a place where you can use other databases as well

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user) # get_queryset() is a method that's built into the model Manager that refers to the queryset methods that you can wrap in as well.


class Product(models.Model):
    # pk 
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/product/{self.pk}/"

    @property
    def body(self):
        return self.content

    def is_public(self):
        return self.public # True or False
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]


    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"

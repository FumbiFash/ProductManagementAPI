from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

# Create your models here.

class ProductQuerySet(models.QuerySet):

    def is_public(self):
        return self.filter(public=True)
        
    def search(self, query, user = None):
        lookup = Q(title__icontains=query) | Q(content__icontains = query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            return qs.filter(user = user)
        return qs


class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using = self._db)

    def search(self, query, user = None):
        # return Product.objects.filter(public=True).filter(title__icontains=query)

        # return self.get_queryset().is_public().search(query,user = user)
        return self.get_queryset().search(query,user = user)


class Product(models.Model):
    user = models.ForeignKey(User, default = 1,on_delete = models.SET_NULL, null = True)
    title = models.CharField(max_length = 120)
    content = models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits = 15,decimal_places = 2, default = 99.9)
    public = models.BooleanField(default=True)
    objects = ProductManager()
    
    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.8)

    
    def get_discount(self):
        return "3443"

   




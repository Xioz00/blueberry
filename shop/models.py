from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Category (models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'



    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_category',args=[self.slug])


class Products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='products')
    description=models.TextField()
    stock=models.IntegerField()
    available = models.BooleanField(default=True)
    my_field = models.DateTimeField(default=timezone.now)
    price=models.IntegerField()
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)


    def get_url(self):
        return reverse('product_details', args=[self.cat.slug, self.slug])

    def __str__ (self):
        return'{}'.format(self.name)


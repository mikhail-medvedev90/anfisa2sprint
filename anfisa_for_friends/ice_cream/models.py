from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)


class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, help_text='Название обёртки')


class IceCream(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')

    class Meta:
        ordering = ('output_order', 'title')

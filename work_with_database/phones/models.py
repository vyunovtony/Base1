from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID телефона')
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.CharField(verbose_name='Ссылка на картинку')
    release_date = models.DateTimeField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


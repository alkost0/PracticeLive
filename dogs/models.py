from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'

class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='кличка')
#    category = models.CharField(max_length=50, verbose_name='порода')
    category = models.ForeignKey(Category, verbose_name='порода', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dogs/', max_length=50, verbose_name='фото', **NULLABLE)
    birthday = models.DateField(verbose_name='дата рождения', **NULLABLE)
#    color = models.CharField(max_length=50, verbose_name='окрас', **NULLABLE)

    def __str__(self):
        return f"{self.name}: {self.category}"

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'


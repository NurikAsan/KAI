from django.db import models
from ckeditor.fields import RichTextField


class AbstractModel(models.Model):
    title = models.CharField(max_length=500, verbose_name='Оглавление')
    image = models.ImageField(
        upload_to='main/news/',
        verbose_name='Изображение'
    )
    text = RichTextField(null=True, blank=True)
    date = models.DateField(verbose_name='Дата')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

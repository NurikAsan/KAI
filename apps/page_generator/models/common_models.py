from django.db import models


class PageGenerator(models.Model):
    image = models.ImageField(
        upload_to='page_generator/',
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

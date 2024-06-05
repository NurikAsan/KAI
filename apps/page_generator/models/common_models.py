from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подкатегория')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='sub_categories'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегрия"
        verbose_name_plural = "Подкатегории"


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подкатегория 2')
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        verbose_name='Подкатегория',
        related_name='sub_sub_categories',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория 2'
        verbose_name_plural = 'Подкатегории 2'


class PageGenerator(models.Model):
    image = models.ImageField(
        upload_to='page-generator/',
        null=True,
        blank=True,
        verbose_name="Баннер"
    )
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Заголовок"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True,
        blank=True
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Подкатегория"
    )
    subcategory2 = models.ForeignKey(
        SubSubCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Подкатегория 2"
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Шаблон страниц"
        verbose_name_plural = "Шаблоны страниц"

# Generated by Django 4.2 on 2024-06-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_generator', '0004_category_subcategory_veteran_alter_documents_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='full_name_en',
        ),
        migrations.RemoveField(
            model_name='person',
            name='full_name_ky',
        ),
        migrations.RemoveField(
            model_name='person',
            name='full_name_ru',
        ),
        migrations.RemoveField(
            model_name='person',
            name='position_en',
        ),
        migrations.RemoveField(
            model_name='person',
            name='position_ky',
        ),
        migrations.RemoveField(
            model_name='person',
            name='position_ru',
        ),
        migrations.AddField(
            model_name='documents',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pdf Файл'),
        ),
        migrations.AddField(
            model_name='veteran',
            name='full_name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='veteran',
            name='full_name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='veteran',
            name='full_name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='veteranposition',
            name='position_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='veteranposition',
            name='position_ky',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='veteranposition',
            name='position_ru',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Полное имя человека'),
        ),
    ]

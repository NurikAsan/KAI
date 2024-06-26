# Generated by Django 4.2 on 2024-06-07 07:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Категория')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Категория')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PageGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='page-generator/', verbose_name='Баннер')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page_generator.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Шаблон страниц',
                'verbose_name_plural': 'Шаблоны страниц',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Полное имя человека')),
                ('full_name_ru', models.CharField(blank=True, max_length=150, null=True, verbose_name='Полное имя человека')),
                ('full_name_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='Полное имя человека')),
                ('full_name_ky', models.CharField(blank=True, max_length=150, null=True, verbose_name='Полное имя человека')),
                ('image', models.ImageField(upload_to='page-generator/', verbose_name='Изображение человека')),
                ('position', models.TextField(blank=True, max_length=150, null=True, verbose_name='Должность человека')),
                ('position_ru', models.TextField(blank=True, max_length=150, null=True, verbose_name='Должность человека')),
                ('position_en', models.TextField(blank=True, max_length=150, null=True, verbose_name='Должность человека')),
                ('position_ky', models.TextField(blank=True, max_length=150, null=True, verbose_name='Должность человека')),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('faks', models.CharField(blank=True, max_length=150, null=True, verbose_name='Факс')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peoples', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Подкатегория')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Подкатегория')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Подкатегория')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Подкатегория')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='page_generator.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегрия',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя таблицы')),
                ('name_ru', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя таблицы')),
                ('name_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя таблицы')),
                ('name_ky', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя таблицы')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Таблица',
                'verbose_name_plural': 'Таблицы',
            },
        ),
        migrations.CreateModel(
            name='TableCodeColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(blank=True, null=True, verbose_name='Код таблицы')),
                ('year', models.PositiveIntegerField(blank=True, default=2000, null=True, verbose_name='Учебный год')),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_codes_column', to='page_generator.table')),
            ],
            options={
                'verbose_name': 'Код и Учебный план таблицы',
                'verbose_name_plural': 'Код и Учебный план таблицы',
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=100, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текстовое описание')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текстовое описание')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текстовое описание')),
                ('description_ky', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текстовое описание')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_contents', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент страниц',
            },
        ),
        migrations.CreateModel(
            name='Veteran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное имя')),
                ('full_name_ru', models.CharField(max_length=100, null=True, verbose_name='Полное имя')),
                ('full_name_en', models.CharField(max_length=100, null=True, verbose_name='Полное имя')),
                ('full_name_ky', models.CharField(max_length=100, null=True, verbose_name='Полное имя')),
                ('image', models.ImageField(upload_to='page-generator/veterans', verbose_name='Изображение')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veterans', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Ветеран',
                'verbose_name_plural': 'Ветераны',
            },
        ),
        migrations.CreateModel(
            name='VeteranPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
                ('position_ru', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
                ('veteran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veteran_positions', to='page_generator.veteran', verbose_name='Ветеран')),
            ],
        ),
        migrations.CreateModel(
            name='TextContentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', utils.fields.WEBPField(blank=True, null=True, upload_to='page-generator/text-content/', verbose_name='Изображение')),
                ('content_text', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text_content_images', to='page_generator.textcontent', verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображение для контента страниц',
            },
        ),
        migrations.CreateModel(
            name='TableDirectionColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.TextField(max_length=200, verbose_name='Направление')),
                ('direction_ru', models.TextField(max_length=200, null=True, verbose_name='Направление')),
                ('direction_en', models.TextField(max_length=200, null=True, verbose_name='Направление')),
                ('direction_ky', models.TextField(max_length=200, null=True, verbose_name='Направление')),
                ('status1', models.CharField(max_length=100)),
                ('status1_ru', models.CharField(max_length=100, null=True)),
                ('status1_en', models.CharField(max_length=100, null=True)),
                ('status1_ky', models.CharField(max_length=100, null=True)),
                ('status2', models.CharField(max_length=100)),
                ('status2_ru', models.CharField(max_length=100, null=True)),
                ('status2_en', models.CharField(max_length=100, null=True)),
                ('status2_ky', models.CharField(max_length=100, null=True)),
                ('links', models.FileField(blank=True, null=True, upload_to='page-generator/', verbose_name='Pdf файл')),
                ('table_code_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_directions_column', to='page_generator.tablecodecolumn')),
            ],
            options={
                'verbose_name': 'Направление таблицы и pdf файлы',
                'verbose_name_plural': 'Направление таблицы и pdf файлы',
            },
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Подкатегория 2')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Подкатегория 2')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Подкатегория 2')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Подкатегория 2')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_sub_categories', to='page_generator.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Подкатегория 2',
                'verbose_name_plural': 'Подкатегории 2',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефон')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='page_generator.person', verbose_name='Владелец')),
            ],
        ),
        migrations.AddField(
            model_name='pagegenerator',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page_generator.subcategory', verbose_name='Подкатегория'),
        ),
        migrations.AddField(
            model_name='pagegenerator',
            name='subcategory2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page_generator.subsubcategory', verbose_name='Подкатегория 2'),
        ),
        migrations.CreateModel(
            name='NavLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('url', models.URLField(verbose_name='URL')),
                ('image', models.ImageField(upload_to='page-generator/', verbose_name='Изображение')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nav_links', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Навигационные ссылки',
                'verbose_name_plural': 'Навигационные ссылки',
            },
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='page-generator/images', verbose_name='Изображение')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images_content', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения для страниц',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pdf Файл')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pdf Файл')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pdf Файл')),
                ('name_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pdf Файл')),
                ('pdf', models.FileField(upload_to='page-generator/documents', verbose_name='Документ')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='page_generator.pagegenerator', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-13 14:29

import ProjectSoftUni.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/', validators=[ProjectSoftUni.common.validators.MaxFileSizeInMbValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('info', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', validators=[ProjectSoftUni.common.validators.MaxFileSizeInMbValidator(5)])),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(),
        ),
    ]

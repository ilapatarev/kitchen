# Generated by Django 4.2.4 on 2024-03-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Cakes', 'cakes'), ('Ice Cream', 'ice cream'), ('Cookies', 'cookies'), ('Candies', 'candies'), ('Pies', 'pies'), ('Tarts', 'tarts'), ('Poudings', 'poudings'), ('Vegan', 'vegan'), ('Other', 'other')], max_length=20),
        ),
    ]

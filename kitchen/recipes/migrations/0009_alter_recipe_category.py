# Generated by Django 4.2.4 on 2024-05-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Cakes', 'Cakes'), ('Ice-Cream', 'Ice-cream'), ('Cookies', 'Cookies'), ('Candies', 'Candies'), ('Pies', 'Cies'), ('Tarts', 'Tarts'), ('Pouddings', 'Pouddings'), ('Vegan', 'Vegan'), ('Other', 'Other')], max_length=20),
        ),
    ]

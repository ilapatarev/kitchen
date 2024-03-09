# Generated by Django 4.2.4 on 2024-03-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_cool_time_alter_recipe_freeze_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('cakes', 'Cakes'), ('icecream', 'Ice Cream'), ('cookies', 'Cookies'), ('candies', 'Candies'), ('pies', 'Pies'), ('tarts', 'Tarts'), ('poudings', 'Poudings'), ('vegan', 'Vegan'), ('other', 'Other')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]

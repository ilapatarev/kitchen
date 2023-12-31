# Generated by Django 4.2.4 on 2023-08-27 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, max_length=5000000, upload_to='recipe_images/')),
                ('prep_time', models.IntegerField(default=0)),
                ('cook_time', models.IntegerField(default=0)),
                ('freeze_time', models.IntegerField(blank=True, default=0, null=True)),
                ('cool_time', models.IntegerField(blank=True, default=0, null=True)),
                ('total_time', models.IntegerField(default=0)),
                ('servings', models.PositiveIntegerField(default=0)),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('tips', models.TextField(blank=True)),
                ('calories', models.PositiveIntegerField(default=0)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbs', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

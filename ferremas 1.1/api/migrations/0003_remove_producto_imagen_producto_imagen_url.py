# Generated by Django 4.2.1 on 2024-05-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

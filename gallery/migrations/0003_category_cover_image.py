# Generated by Django 3.2.6 on 2021-08-23 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210822_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover_image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.photo'),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_bookorder_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='books/empty_cover.jpg', upload_to='books/'),
        ),
    ]
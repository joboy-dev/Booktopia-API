# Generated by Django 4.1.7 on 2023-06-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_book_average_rating_alter_book_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
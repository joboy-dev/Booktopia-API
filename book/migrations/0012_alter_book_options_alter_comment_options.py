# Generated by Django 4.1.7 on 2023-06-17 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_rename_comments_book_no_of_comments_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated']},
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-10 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_rename_product_order_book_order_download_token_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book',
            new_name='product',
        ),
    ]
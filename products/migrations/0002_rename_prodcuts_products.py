# Generated by Django 4.1.1 on 2022-10-21 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catagory", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Prodcuts",
            new_name="Products",
        ),
    ]

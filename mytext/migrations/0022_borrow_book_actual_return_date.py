# Generated by Django 4.2.9 on 2024-01-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mytext", "0021_alter_borrow_book_returned"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrow_book",
            name="actual_return_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]

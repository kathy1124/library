# Generated by Django 5.0.1 on 2024-01-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytext', '0019_alter_borrow_book_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_book',
            name='returned',
            field=models.CharField(choices=[('已歸還', '已歸還'), ('尚未歸還', '尚未歸還')], max_length=10),
        ),
    ]

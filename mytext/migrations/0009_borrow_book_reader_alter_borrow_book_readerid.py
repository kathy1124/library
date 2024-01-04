# Generated by Django 4.2.5 on 2024-01-04 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mytext', '0008_rename_borrow_books_borrow_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow_book',
            name='reader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='readerID',
            field=models.CharField(max_length=10),
        ),
    ]

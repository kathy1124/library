# Generated by Django 4.2.5 on 2024-01-04 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mytext', '0010_alter_post_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow_book',
            name='reader',
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='readerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.4 on 2024-01-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytext', '0003_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
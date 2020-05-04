# Generated by Django 3.0.5 on 2020-04-20 17:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="comp",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="techno",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="techno", name="name", field=models.TextField(unique=True),
        ),
    ]

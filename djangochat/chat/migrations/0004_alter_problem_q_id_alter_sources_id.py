# Generated by Django 4.1.3 on 2022-12-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="q_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="sources",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

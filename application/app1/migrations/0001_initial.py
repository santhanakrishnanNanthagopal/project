# Generated by Django 5.1.6 on 2025-05-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=30)),
                ('sub_category', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField(max_length=10)),
            ],
        ),
    ]

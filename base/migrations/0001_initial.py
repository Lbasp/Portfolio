# Generated by Django 4.1.7 on 2023-04-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('resumen', models.TextField()),
                ('page_url', models.URLField()),
                ('gif_url', models.URLField()),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('field_name', models.BooleanField()),
                ('area', models.CharField(choices=[('DS', 'Data Science'), ('PD', 'Product Development'), ('RS', 'Research')], max_length=2)),
                ('skills', models.TextField()),
            ],
        ),
    ]

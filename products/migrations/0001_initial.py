# Generated by Django 5.0.6 on 2024-09-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img')),
                ('base_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
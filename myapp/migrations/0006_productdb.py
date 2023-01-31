# Generated by Django 4.1.2 on 2022-12-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_categorydb_delete_empdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('productname', models.CharField(blank=True, max_length=30, null=True)),
                ('discription', models.CharField(blank=True, max_length=100, null=True)),
                ('productprice', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20)),
                ('os_type', models.CharField(max_length=30)),
                ('server_type', models.CharField(max_length=30)),
            ],
        ),
    ]

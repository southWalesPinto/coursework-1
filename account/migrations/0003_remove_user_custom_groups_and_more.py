# Generated by Django 5.0.3 on 2024-05-01 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='custom_groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='custom_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='profile_pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]

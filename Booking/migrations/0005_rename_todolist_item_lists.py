# Generated by Django 5.0.3 on 2024-04-19 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_alter_todolist_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='todolist',
            new_name='lists',
        ),
    ]

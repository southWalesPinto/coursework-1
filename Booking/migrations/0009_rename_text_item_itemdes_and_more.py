# Generated by Django 5.0.3 on 2024-04-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_rename_list_saveditem_lists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='itemDes',
        ),
        migrations.RenameField(
            model_name='unsaveditem',
            old_name='text',
            new_name='itemDes',
        ),
        migrations.RemoveField(
            model_name='saveditem',
            name='text',
        ),
        migrations.AddField(
            model_name='item',
            name='itemName',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='itemRentalPeriod',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='item',
            name='itemType',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='saveditem',
            name='itemDes',
            field=models.CharField(default=True, max_length=300),
        ),
        migrations.AddField(
            model_name='saveditem',
            name='itemName',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='saveditem',
            name='itemRentalPeriod',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='saveditem',
            name='itemType',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='unsaveditem',
            name='itemName',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='unsaveditem',
            name='itemRentalPeriod',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='unsaveditem',
            name='itemType',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
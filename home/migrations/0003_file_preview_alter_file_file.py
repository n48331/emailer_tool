# Generated by Django 4.1.3 on 2022-12-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_country_rename_country_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='Files/preview'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Files/projects'),
        ),
    ]

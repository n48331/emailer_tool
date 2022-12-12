# Generated by Django 4.1.3 on 2022-12-01 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='country',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productId',
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=50)),
                ('file', models.FileField(blank=True, null=True, upload_to='Files')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.country')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]

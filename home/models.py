from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


def project_filename(instance, filename):
    filename_ = instance.productId
    file_extension = filename.split('.')[-1]
    return 'Files/projects/%s.%s' % (filename_, file_extension)


def preview_filename(instance, filename):
    filename_ = instance.productId
    file_extension = filename.split('.')[-1]
    return 'Files/preview/%s.%s' % (filename_, file_extension)


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class File(models.Model):
    productId = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(null=False, blank=False,
                            upload_to=project_filename)
    preview = models.FileField(
        null=True, blank=True, upload_to=preview_filename)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.productId + " || " + self.country.name + " || " + self.product.name

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            instance_file_field = getattr(instance, field.name)
            delete_file_if_unused(sender, instance, field, instance_file_field)


""" Delete the file if something else get uploaded in its place"""


@receiver(pre_save)
def delete_files_when_file_changed(sender, instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            # its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db, field.name)
            instance_file_field = getattr(instance, field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(
                    sender, instance, field, instance_in_db_file_field)


""" Only delete the file if no other instances of that model are using it"""


def delete_file_if_unused(model, instance, field, instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(
        **dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)

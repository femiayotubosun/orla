from distutils.command.upload import upload
import imp
from io import BytesIO
from PIL import Image

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.files import File
from orla.settings import BASE_URL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})

    def get_image(self):
        if self.image:
            return BASE_URL + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return BASE_URL + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumnail(self.image)
                self.save()
                return BASE_URL + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "PNG", quality="85")
        thumbnail = File(thumb_io, name=f"category_thumbnail_{image.name}")
        return thumbnail


# FIXME IMAGES!!


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def get_image(self):
        if self.image:
            return BASE_URL + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return BASE_URL + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumnail(self.image)
                self.save()
                return BASE_URL + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "PNG", quality="85")
        thumbnail = File(thumb_io, name=f"product_thumbnail_{image.name}")
        return thumbnail

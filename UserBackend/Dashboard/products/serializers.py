import uuid

from django.db import models

# Create your models here.

class Product(models.Model):
    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    id = models.UUIDField(
        primary_key=True,
        blank=False,
        null=False,
        default=uuid.UUID,
        editable=False,
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=200,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    company = models.ForeignKey(
        null=False,
        blank=False,
    )
    categories = models.ForeignKey(
        null=False,
        blank=False,
    )
    sub_categories= models.ForeignKey(
        null=False,
        blank=False,
    )
    manufacturer = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

class Categories(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class SubCategories(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    category = models.ForeignKey(
        Categories,
        on_delete=True
    )

    class Meta:
        db_table = "subcategories"
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"




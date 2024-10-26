from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _

class CategoryModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Category Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class TagModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Tag Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class BrandModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Brad Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brand")


class SizeModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Size Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class ColourModel(BaseModel):
    code = models.CharField(max_length=255, verbose_name=_("Color Code"))
    name = models.CharField(max_length=255, verbose_name=_("Color Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class ProductModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Product Name"))
    stock = models.BooleanField(verbose_name=_("Stock"))
    image1 = models.ImageField(upload_to="products/")
    image2 = models.ImageField(upload_to="products/")
    short_description = models.TextField()
    long_description = models.TextField()
    sku = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    real_price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ManyToManyField(CategoryModel, related_name='products')
    tags = models.ManyToManyField(TagModel, related_name='products')
    sizes = models.ManyToManyField(SizeModel, related_name='products')
    colours = models.ManyToManyField(ColourModel, related_name='products')

    brands = models.ForeignKey(BrandModel, related_name='products', on_delete=models.CASCADE)

    def is_discount(self):
        return True if self.discount != 0 else False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _('Products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

from rest_framework import serializers
from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category_slug = serializers.SlugField(source="category.slug", read_only=True)
    category_absolute_url = serializers.CharField(
        source="category.get_absolute_url", read_only=True
    )
    slug = serializers.ReadOnlyField()
    absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "absolute_url",
            "category_slug",
            "category_absolute_url",
            "image",
            "get_image",
            "get_thumbnail",
        ]
        extra_kwargs = {"image": {"write_only": True}}


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    slug = serializers.ReadOnlyField()
    absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "absolute_url",
            "products",
            "image",
            "get_image",
            "get_thumbnail",
        ]
        extra_kwargs = {"image": {"write_only": True}}

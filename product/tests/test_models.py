import unittest
from django.test import TestCase
from product.models import Category, Product


class CategoryTest(TestCase):
    def test_category_create_should_add_to_db_successfully(self):
        cats = Category.objects.all().count()
        category: Category = Category.objects.create(name="Test Category")
        self.assertEqual(cats + 1, Category.objects.all().count())

    def test_category_slug_should_slugify_successfully(self):
        cat = Category.objects.create(name="Test Category")

        self.assertEqual("test-category", cat.slug)

    def test_category__str__(self):
        cat = Category.objects.create(name="Test Cat")

        self.assertEqual(cat.__str__(), "Test Cat")

    @unittest.skip("Yet to setup urls")
    def test_category_absolute_url(self):
        pass


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.category: Category = Category.objects.create(name="Test Category")

    def test_create_product_without_category_should_throw_error(self) -> None:

        with self.assertRaises(Exception):
            product: Product = Product.objects.create(name="Product")

    def test_create_product_should_add_to_db(self) -> None:
        old_products = Product.objects.all().count()
        product = Product.objects.create(
            name="Test Prod", category=self.category, price=1.34
        )

        self.assertEqual(old_products + 1, Product.objects.all().count())

    def test_test_product_str(self) -> None:
        product = Product.objects.create(
            name="Test Prod", category=self.category, price=1.34
        )

        self.assertEqual(product.__str__(), "Test Prod")

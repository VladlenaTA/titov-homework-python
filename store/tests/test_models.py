from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    #def setUp(self):
        #self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        data = self.data
        self.assertEqual(str(data), 'Harry potter')


class TestProductsModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='Harry potter', slug='harry-potter')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create()

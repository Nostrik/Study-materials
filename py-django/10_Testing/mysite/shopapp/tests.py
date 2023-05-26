from string import ascii_letters
from random import choices

from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse
# from shopapp.utils import add_two_numbers
from shopapp.models import Product, Order


# class AddTwoNumbersTestCase(TestCase):
#     def test_add_two_numbers(self):
#         result = add_two_numbers(2, 3)
#         self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123.45",
                "description": "A good table",
                "discount": "10",
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="Base Product")

    # def setUp(self) -> None:
    #     self.product = Product.objects.create(name="Base Product")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    # def tearDown(self) -> None:
    #     self.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestVase(TestCase):
    fixtures = [
        'products-fixtures.json'
    ]

    def test_products(self):
        response = self.client.get(reverse("shopapp:products_list"))
        for product in Product.objects.filter(archived=False).all():
            self.assertContains(response, product.name)
            
    # def test_products(self):
    #     response = self.client.get(reverse("shopapp:products_list"))
    #     self.assertQuerysetEqual(
    #         qs=Product.objects.filter(archived=True).all(),
    #         values=(p.pk for p in response.context["products"]),
    #         transform=lambda p: p.pk,
    #     )
    #     self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrdersListView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username="bob_test", password="qwerty")
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse("shopapp:orders_list"))
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:orders_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixtures.json'
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:products-export"),
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": str(product.price),
                "archived": product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data,
        )


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username="user_test", password="pwd_tst")
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        permission = Permission.objects.get_by_natural_key('shopapp:view_order', 'tests', 'order')
        self.user.
        self.client.force_login(self.user)
        self.order = Order.objects.create(delivery_address='123 Main St', promocode='SUMMER', user=self.user)

    def tearDown(self):
        self.order.delete()

    def test_order_details(self):
        url = reverse("shopapp:order_details", kwargs={'pk': self.order.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.address)
        self.assertContains(response, self.order.promo_code)
        self.assertEqual(response.context['object'], self.order)

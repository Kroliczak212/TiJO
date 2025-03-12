import unittest
from ..src.shopping_cart import shopping_cart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = shopping_cart()
        self.sample_product = ("Laptop", 3000, 1)
        self.valid_discount_code = "BLACKFRIDAY"

    # Testy dla add_product()
    def test_add_product_success(self):
        # Arrange
        product_name, price, quantity = self.sample_product

        # Act
        result = self.cart.add_product(product_name, price, quantity)

        # Assert
        self.assertTrue(result)
        self.assertIn(product_name, self.cart.get_products())

    def test_add_duplicate_product_failure(self):
        # Arrange
        self.cart.add_product(*self.sample_product)

        # Act
        result = self.cart.add_product(*self.sample_product)

        # Assert
        self.assertFalse(result)
        self.assertEqual(self.cart.count_products(), 1)

    # Testy dla remove_product()
    def test_remove_product_success(self):
        # Arrange
        self.cart.add_product(*self.sample_product)

        # Act
        result = self.cart.remove_product(self.sample_product[0])

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.count_products(), 0)

    def test_remove_nonexistent_product_failure(self):
        # Act & Assert
        self.assertFalse(self.cart.remove_product("Nieistniejacy produkt"))

    # Testy dla update_quantity()
    def test_update_quantity_success(self):
        # Arrange
        self.cart.add_product(*self.sample_product)
        new_quantity = 3

        # Act
        result = self.cart.update_quantity(self.sample_product[0], new_quantity)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.get_total_price(), 3000 * new_quantity)

    def test_update_quantity_to_zero_removes_product(self):
        # Arrange
        self.cart.add_product(*self.sample_product)

        # Act
        result = self.cart.update_quantity(self.sample_product[0], 0)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.count_products(), 0)

    # Testy dla get_products()
    def test_get_products_empty_cart(self):
        self.assertEqual(self.cart.get_products(), [])

    # Testy dla count_products()
    def test_count_products_empty_cart(self):
        self.assertEqual(self.cart.count_products(), 0)

    # Testy dla get_total_price()
    def test_total_price_empty_cart(self):
        self.assertEqual(self.cart.get_total_price(), 0)

    def test_total_price_with_discount(self):
        # Arrange
        self.cart.add_product(*self.sample_product)
        self.cart.apply_discount_code(self.valid_discount_code)

        # Act & Assert
        expected_total = int(3000 * 0.8)  # 20% rabatu
        self.assertEqual(self.cart.get_total_price(), expected_total)

    # Testy dla checkout()
    def test_checkout_success(self):
        # Arrange
        self.cart.add_product(*self.sample_product)

        # Act & Assert
        self.assertTrue(self.cart.checkout())
        self.assertEqual(self.cart.count_products(), 0)


if __name__ == "__main__":
    unittest.main()
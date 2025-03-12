class shopping_cart:
    def __init__(self):
        self.products = {}  # Format: {product_name: (price, quantity)}
        self.discount = 1.0
        self.valid_discount_codes = {"BLACKFRIDAY": 0.8}  # 20% zniżki

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if product_name in self.products or quantity <= 0:
            return False
        self.products[product_name] = (price, quantity)
        return True

    def remove_product(self, product_name: str) -> bool:
        if product_name not in self.products:
            return False
        del self.products[product_name]
        return True

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name not in self.products:
            return False
        if new_quantity <= 0:
            del self.products[product_name]
        else:
            price, _ = self.products[product_name]
            self.products[product_name] = (price, new_quantity)
        return True

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return len(self.products)

    def get_total_price(self) -> int:
        total = sum(price * quantity for price, quantity in self.products.values())
        return int(total * self.discount)

    def apply_discount_code(self, discount_code: str) -> bool:
        if discount_code in self.valid_discount_codes:
            self.discount = self.valid_discount_codes[discount_code]
            return True
        self.discount = 1.0
        return False

    def checkout(self) -> bool:
        if not self.products:
            return False
        self.products.clear()
        self.discount = 1.0
        return True
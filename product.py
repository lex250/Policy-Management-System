# Creating the Product class with update, suspend, remove and display details methods.

class Product:
    product_catalog = {}

    def __init__(self, product_id, name, price):
        """Initialize a new product with ID, name, and price."""
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = True  # Product is active by default
        Product.product_catalog[product_id] = self

    @staticmethod
    def get_product_by_id(product_id):
        """Fetch product details by ID."""
        return Product.product_catalog.get(product_id)

    def update(self, name=None, price=None):
        """Update the product's name and/or price."""
        if name:
            self.name = name
            print(f"Name of Product {self.product_id} has been updated to '{name}'")
        if price:
            self.price = price
            print(f"Price of Product {self.product_id} has been updated to {price}")

    def suspend_product(self):
        """Suspend the product."""
        self.active = False
        print(f"This product: {self.name} is not available at the moment")

    def reactivate_product(self):
        """Reactivate suspended product"""
        if not self.active:
            self.active = True
            print(f"The product '{self.name}' is now available!")
        else:
            print(f"This product: {self.name} is already available!")           

    def display_details(self):
        """Display the product's details."""
        status = "Active" if self.active else "Suspended"
        print(f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Status: {status}")
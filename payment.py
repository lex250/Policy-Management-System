# Creating the Payment class and process payment, send reminder and apply penalty methods

# To enable utilization of data from the product.py file
from product import Product 

class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount):
        """Initialize a new payment with payment ID, policyholder ID, product ID, and amount."""
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.payment_history = {}

    def process_payment(self):
        """Process the payment."""
        product = Product.get_product_by_id(self.product_id)  # Get Product data from the Product class
        if not product:
            print(f"Product ID {self.product_id} not found.")
            return

        if self.amount == product.price:
            self.payment_history[self.payment_id] = self.amount
            print(f"Processing payment of {self.amount} for policyholder {self.policyholder_id} for product {self.product_id} ({product.name})")
        else:
            print(f"Payment unsuccessful! Kindly input correct product price: {product.price}")

    def send_reminder(self, days_left):
        """Send payment reminder."""
        if days_left in [7, 3, 1]:
            print(f"Sending payment reminder to policyholder {self.policyholder_id} for product {self.product_id} ({Product.get_product_by_id(self.product_id).name}). Payment due in {days_left} days.")

    def apply_penalty(self, penalty_amount):
        """Apply a penalty to the payment."""
        self.amount += penalty_amount
        print(f"Applied penalty of {penalty_amount}. New amount due: {self.amount}")

    @staticmethod
    def display_account_details(payments, policyholders, products):
        for payment in payments:
            policyholder = next((ph for ph in policyholders if ph.policyholder_id == payment.policyholder_id), None)
            product = next((pr for pr in products if pr.product_id == payment.product_id), None)
            if policyholder and product:
                print(f"Policyholder Name: {policyholder.name}")
                print(f"Email: {policyholder.email}")
                print(f"Product: {product.name}")
                print(f"Amount Paid: {payment.amount}")
                print("-" * 40)
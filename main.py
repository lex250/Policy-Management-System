# main.py

from policyholder import Policyholder
from product import Product
from payment import Payment

def main():
    # Creating the two policyholders accounts
    policyholder1 = Policyholder(policyholder_id=1, name="Lesley Jerry", email="lesleyjerry@otp.com")
    policyholder2 = Policyholder(policyholder_id=2, name="Nnanke Bassey", email="nnankebassey@otp.com")

    # Display both policyholders details
    print("\nBelow are the details of the policyholders created")
    policyholder1.display_details()
    policyholder2.display_details()

    # Create two products with the products class
    product1 = Product(product_id=1, name="Car Insurance", price=200000.0)
    product2 = Product(product_id=2, name="House Insurance", price=500000.0)

    # Display the products details
    print("\nBelow are the details of the two products created")
    product1.display_details()
    product2.display_details()

    # Creating payments for the two policyholders with the payment class.
    payment1 = Payment(payment_id=1, policyholder_id=1, product_id=1, amount=200000.0)
    payment2 = Payment(payment_id=2, policyholder_id=2, product_id=2, amount=500000.0)
    payment3 = Payment(payment_id=3, policyholder_id=2, product_id=2, amount=400000.0)  # This is to test for wrong payment amount

    # Process the payments
    print("\nBelow are receipts for product payment")
    payment1.process_payment()
    payment2.process_payment()
    payment3.process_payment()  # This should throw up a curated error message

    # Store all instances in lists
    payments = [payment1, payment2]
    policyholders = [policyholder1, policyholder2]
    products = [product1, product2]

    # Display account details for policyholders who have made payments
    print("\n\nAccount Details for Policyholders with Payments:\n")
    Payment.display_account_details(payments, policyholders, products)

    # Send payment reminders
    print("\nBelow reminders to be sent to Policyholders")
    payment1.send_reminder(days_left=7)
    payment2.send_reminder(days_left=3)
    payment1.send_reminder(days_left=1)

    # Apply penalties
    print("\nBelow penalties to be applied for late payment of products: Car Insurance and House Insurance respectively.")
    payment1.apply_penalty(5000)
    payment2.apply_penalty(10000)

    # Suspend and reactivate policyholder1 account
    print("\nThe policyholder below has been suspended")
    policyholder1.suspend()
    policyholder1.display_details()
    print("\nThe policyholder below has been reactivated")
    policyholder1.reactivate()
    policyholder1.display_details()

    # Suspend and reactivate product1
    print("\nThe product below has been suspended")
    product1.suspend_product()
    product1.display_details()
    print("\nThe product has later been reactivated")
    product1.reactivate_product()
    product1.display_details()

    # Test reactivating an already active product and policyholder
    print("\nAttempt to reactivate an already active product")
    product2.reactivate_product()
    product2.display_details()
    print("\nAttempt to reactivate an already active policyholder")
    policyholder2.reactivate()
    policyholder2.display_details()

    # Update product1 price and display the details
    print("\nBelow shows product price update")
    product1.update(price=250000.0)
    product1.display_details()

if __name__ == "__main__":
    main()
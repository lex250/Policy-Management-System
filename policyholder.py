# Creating the Policyholder class with registration, suspend, reactivate and display details methods

class Policyholder:
    def __init__(self, policyholder_id, name, email):
        """Initialize a new policyholder with ID, name, and email."""
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.active = True  # Policyholder is active by default

    def suspend(self):
        """Suspend the policyholder's account."""
        if self.name:
            self.active = False
            print(f"Hello {self.name}, your account has been suspended due to payment default.")    

    def reactivate(self):
        """Reactivate the policyholder's account."""
        if not self.active:
            self.active = True
            print(f"Congrats, {self.name}! Your account has been reactivated!")
        else:
            print(f"{self.name}, your account is already active!")        

    def display_details(self):
        """Display the policyholder's details."""
        status = "Active" if self.active else "Suspended"
        print(f"ID: {self.policyholder_id}, Name: {self.name}, Email: {self.email}, Status: {status}")
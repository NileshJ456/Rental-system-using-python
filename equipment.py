from datetime import datetime, timedelta

class Equipment:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.rental_date = None  # Initialize rental_date as None

    def rent(self):
        if self.rental_date is None:
            self.rental_date = datetime.now()

    def return_equipment(self):
        self.rental_date = None  # Reset rental_date when equipment is returned

    

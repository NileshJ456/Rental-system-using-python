from datetime import datetime, timedelta
from equipment import Equipment

class RentalSystem:
    def __init__(self):
        self.equipment_list = []
        self.load_equipment_data()

    def load_equipment_data(self):
        with open("equipment_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(", ")
                equipment = Equipment(data[0], data[1], float(data[2][1:]), int(data[3]))
                self.equipment_list.append(equipment)

    def find_equipment(self, equipment_name):
        for equipment in self.equipment_list:
            if equipment.name == equipment_name:
                return equipment
        return None

    def update_equipment_stock(self, equipment, quantity):
        equipment.quantity -= quantity

    def rent_equipment(self, customer_name, equipment_name, quantity):
        rental_date = datetime.now()
        return_date = rental_date + timedelta(days=5)
        total_amount = 0.0

        equipment = self.find_equipment(equipment_name)
        if equipment is not None and equipment.quantity >= quantity:
            total_amount = equipment.price * quantity
            equipment.rental_date = rental_date
            self.update_equipment_stock(equipment, quantity)

            invoice = f"Rental Invoice\nCustomer: {customer_name}\nEquipment: {equipment_name} ({quantity} units)\nRental Date: {rental_date}\nReturn Date: {return_date}\nTotal Amount: ${total_amount:.2f}\n\n"
            with open(f"{customer_name}_rental_invoice.txt", "a") as file:
                file.write(invoice)
        else:
            print("Equipment not available for rental.")

    def return_equipment(self, customer_name, equipment_name):
        return_date = datetime.now()
        fine_per_day = 10  # Example fine amount per day
        total_amount = 0.0

        equipment = self.find_equipment(equipment_name)
        if equipment is not None and equipment.rental_date is not None:
            rental_duration = (return_date - equipment.rental_date).days
            fine = max(0, rental_duration - 5) * fine_per_day
            total_amount = equipment.price * rental_duration + fine
            equipment.rental_date = None
            self.update_equipment_stock(equipment, 1)

            invoice = f"Return Invoice\nCustomer: {customer_name}\nEquipment: {equipment_name}\nReturn Date: {return_date}\nTotal Amount: ${total_amount:.2f}\n\n"
            with open(f"{customer_name}_return_invoice.txt", "a") as file:
                file.write(invoice)
        else:
            print("This equipment is not currently rented.")

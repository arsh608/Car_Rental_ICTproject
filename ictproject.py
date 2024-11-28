from datetime import date, timedelta

class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.__rental_price = rental_price
        self.is_available = True

    def get_rental_price(self):
        return self.__rental_price

    def check_availability(self):
        return self.is_available

    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
        else:
            raise Exception("Vehicle is not available for rent.")

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return days * self.get_rental_price()

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Price per day: ${self.get_rental_price()}, Available: {self.is_available}")


class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        super().display_details()


class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        super().display_details()


class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def display_details(self):
        super().display_details()


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
        self.rental_history = []

    def get_contact_info(self):
        return self.__contact

    def add_rental_history(self, reservation):
        self.rental_history.append(reservation)

    def display_rental_history(self):
        print(f"Rental History for {self.name}:")
        for reservation in self.rental_history:
            reservation.display_reservation_details()


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def calculate_total_cost(self):
        rental_days = (self.end_date - self.start_date).days + 1
        return self.vehicle.calculate_rental_cost(rental_days)

    def display_reservation_details(self):
        print(f"Customer: {self.customer.name}")
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"Rental Period: {self.start_date} to {self.end_date}")
        print(f"Total Cost: ${self.calculate_total_cost()}")
        print(f"Vehicle Availability: {self.vehicle.check_availability()}")

    def rent(self):
        self.vehicle.rent_vehicle()

    def return_vehicle(self):
        self.vehicle.return_vehicle()


def display_info(item):
    item.display_details()

"""
car1 = Car("Toyota", "Corolla", 50)
suv1 = SUV("Jeep", "Wrangler", 80)
truck1 = Truck("Ford", "F-150", 120)

customer1 = Customer("John Doe", "abc@example.com")
customer2 = Customer("Jane Smith", "efc@example.com")

reservation1 = RentalReservation(customer1, car1, date(2024, 9, 1), date(2024, 9, 5))
reservation2 = RentalReservation(customer2, suv1, date(2024, 9, 3), date(2024, 9, 7))

reservation1.rent()
reservation2.rent()

display_info(car1)#vehicle info
display_info(suv1)
display_info(truck1)

reservation1.display_reservation_details()#reservation details
reservation2.display_reservation_details()

customer1.add_rental_history(reservation1)#customer history
customer2.add_rental_history(reservation2)

reservation1.return_vehicle()#return vehicle

customer1.display_rental_history()#rental history
customer2.display_rental_history()
"""
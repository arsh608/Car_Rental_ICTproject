import os
from ictproject import Car, SUV, Truck, Customer, RentalReservation, Vehicle
from datetime import datetime


class RentalSystem:
    FILENAME = "rental_history.txt"

    def __init__(self, vehicles):
        self.vehicles = vehicles

    def save_rental_to_file(self, reservation):
        with open(self.FILENAME, "a") as file:
            file.write(f"{reservation.customer.name},{reservation.vehicle.make},{reservation.vehicle.model},"
                       f"{reservation.start_date},{reservation.end_date},"
                       f"{reservation.calculate_total_cost()}\n")

    def read_rental_history(self):
        if not os.path.exists(self.FILENAME):
            print("No rental history found.")
            return

        print("\nRental History from File:")
        with open(self.FILENAME, "r") as file:
            for line in file:
                name, make, model, start_date, end_date, total_cost = line.strip().split(",")
                print(f"Customer: {name}, Vehicle: {make} {model}, Rental Period: {start_date} to {end_date}, "
                      f"Total Cost: ${total_cost}")

    def rent_vehicle(self):
        print("\nAvailable Vehicles:")
        for i, vehicle in enumerate(self.vehicles, start=1):
            print(f"{i}. {vehicle.make} {vehicle.model} - ${vehicle.get_rental_price()} per day - "
                  f"Available: {vehicle.is_available}")

        try:
            choice = int(input("Select a vehicle (by number): ")) - 1
            if choice not in range(len(self.vehicles)):
                raise ValueError("Invalid choice.")
            vehicle = self.vehicles[choice]

            if not vehicle.check_availability():
                print("Vehicle is not available for rent.")
                return

            customer_name = input("Enter customer name: ")
            customer_email = input("Enter customer email: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

            customer = Customer(customer_name, customer_email)
            reservation = RentalReservation(customer, vehicle, start_date, end_date)
            reservation.rent()
            customer.add_rental_history(reservation)
            self.save_rental_to_file(reservation)

            print("Vehicle rented successfully!")
            reservation.display_reservation_details()

        except Exception as e:
            print(f"Error: {e}")

    def return_vehicle(self):
        """Return a vehicle."""
        vehicle_make = input("Enter the make of the vehicle: ").upper()
        vehicle_model = input("Enter the model of the vehicle: ").upper()

        for vehicle in self.vehicles:
            if vehicle.make == vehicle_make and vehicle.model == vehicle_model:
                if vehicle.is_available:
                    print("This vehicle is already returned.")
                else:
                    vehicle.return_vehicle()
                    print("Vehicle returned successfully!")
                return

        print("Vehicle not found. Please check the details and try again.")

    def main_menu(self):
        """Display the main menu and handle user inputs."""
        while True:
            print("\n--- Vehicle Rental System ---")
            print("1. Rent a Vehicle")
            print("2. Return a Vehicle")
            print("3. View Rental History")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.rent_vehicle()
            elif choice == "2":
                self.return_vehicle()
            elif choice == "3":
                self.read_rental_history()
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


car1 = Car("TOYOTA", "COROLLA", 50)
suv1 = SUV("JEEP", "WRANGLER", 80)
truck1 = Truck("FORD", "BUAN", 120)

car2 = Car("HONDA", "CIVIC", 55)
suv2 = SUV("TOYOTA", "LAND CRUISER", 90)
truck2 = Truck("CHEVROLET", "SILVERADO", 130)

rental_system = RentalSystem([car1, car2, suv1, suv2, truck1, truck2])

if __name__ == "__main__":
    rental_system.main_menu()

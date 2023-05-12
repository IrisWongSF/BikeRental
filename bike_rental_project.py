import csv

class Bike_Rental:
    def __init__(self):
        self.stock = self.read_stock_from_file()

    def read_stock_from_file(self):
        with open("stock.csv", "r") as file:
            reader = csv.reader(file)
            stock = {}
            for row in reader:
                item = row[0]
                quantity = int(row[1])
                stock[item] = quantity
            return stock

    def write_stock_to_file(self):
        with open("stock.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for item, quantity in self.stock.items():
                writer.writerow([item, quantity])

    def rental(self, rental_type, quantity):
        if rental_type not in self.stock:
            print('Invalid rental type')
            return

        if quantity > self.stock[rental_type]:
            print('Sorry, we do not have enough bikes')
            return

        if rental_type == 'hourly':
            cost = 5 * quantity
            self.stock[rental_type] -= quantity
        elif rental_type == 'daily':
            cost = 20 * quantity
            self.stock[rental_type] -= quantity
        elif rental_type == 'weekly':
            cost = 60 * quantity
            self.stock[rental_type] -= quantity
        self.write_stock_to_file()
        print('The total rental amount is: $', cost)
        return cost


    def return_bike(self):
        return_type = input("What type of bikes do you want to return?\n"
                            "Input '1' for hourly basis\n"
                            "Input '2' for daily basis\n"
                            "Input '3' for weekly basis: ")
        if return_type == '1':
            return_type = 'hourly'
        elif return_type == '2':
            return_type = 'daily'
        elif return_type == '3':
            return_type = 'weekly'
        else:
            print('Invalid rental type')
            return

        quantity = int(input("Enter the number of bikes you want to return: "))
        cost =None
        if return_type not in self.stock:
            print('Invalid rental type')
            return
        if return_type == 'hourly':
            cost = 5 * quantity
        elif return_type == 'daily':
            cost = 20 * quantity
        elif return_type == 'weekly':
            cost = 60 * quantity
        self.write_stock_to_file()

        self.stock[return_type] += quantity
        self.write_stock_to_file()
        if cost is not None :
            cost = self.family_rental(quantity, cost)
            print(f"You rented {quantity} bikes, cost you ${cost}")
            return self.stock

    def display_stock(self):
        print('Current stock:')
        for item, quantity in self.stock.items():
            print(item, ':', quantity)

    def family_rental(self, rental_quantity, rental_cost):
        if rental_quantity >= 3:
            cost = rental_cost * 0.7
        else:
            cost = rental_cost

        print('The discounted total rental amount is: $', cost)
        return cost

    def receipt(self):
        print("Welcome to Excellent Bike Rental Shop")
        rental_type = input("What type of bikes do you want to rent?\n"
                        "Input '1' for hourly basis\n"
                        "Input '2' for daily basis\n"
                        "Input '3' for weekly basis: ")
        quantity = int(input("Enter the number of bikes you want to rent: "))

        if rental_type == '1':
            rental_type = 'hourly'
        elif rental_type == '2':
            rental_type = 'daily'
        elif rental_type == '3':
            rental_type = 'weekly'
        else:
            print('Invalid rental type')
            return

        cost = self.rental(rental_type, quantity)
        if cost is not None:
            cost = self.family_rental(quantity, cost)
            print(f"You rented {quantity} bikes, cost you ${cost}")


def main():
    bool = True
    bike_shop = Bike_Rental()
    while bool:
        customer_input = int(input("What do you want to do today?\n"
                                   "Input '1' for displaying bikes\n"
                                   "Input '2' for renting bikes\n"
                                   "Input '3' for returning bikes\n"
                                   "Input '4' exit service: "))
        if customer_input == 1:
            bike_shop.display_stock()
        elif customer_input == 2:
            bike_shop.receipt()
        elif customer_input == 3:
            print("return bike")
            bike_shop.stock = bike_shop.return_bike()

        elif customer_input == 4:
            bool = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

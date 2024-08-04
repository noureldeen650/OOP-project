import csv
class Item:
    def __init__(self,name: str ,price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

        assert self.price >= 0, "Price must be zero or greater"
        assert self.quantity >= 0, "Quantity must be zero or greater"
    def calculate_total_price(self):
        return self.price*self.quantity

    def calculate_discount(self, pay_rate: float):
        assert 0<= pay_rate<=1
        return self.price *(1-pay_rate)

    def __str__(self):
        return f"Item(name: {self.name}, price: {self.price:.2f}, quantity: {self.quantity})"

    def __repr__(self):

        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

     def read_data_from_csv(cls, file_path: str):
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Item(
                        name=row['name'],
                        price=float(row['price']),
                        quantity=int(row['quantity'])
                    )

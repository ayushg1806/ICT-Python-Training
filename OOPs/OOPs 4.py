#Inventory Class with Item Management and Reporting

class Inventory():
    def __init__(self, item_id, item_name, quantity, price):
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
    
    def add_item(self, quantity):
        self.quantity += quantity
        print(f'Added {quantity} of {self.item_name}, New quantity: {self.quantity}')
    
    def remove_item(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f'Removed {quantity} of {self.item_name}, New quantity: {self.quantity}')
        else:
            print('Insufficient quantity to remove.')
    
    def update_item(self, item_name=None, price=None):
        if item_name:
            self.item_name = item_name
        if price:
            self.price = price
        print(f'Updated item: {self.item_name}, Price: {self.price}')
    
    def check_item_details(self):
        print(f'Item ID: {self.item_id}')
        print(f'Item Name: {self.item_name}')
        print(f'Quantity: {self.quantity}')
        print(f'Price: {self.price}')

item1 = Inventory('001', 'Laptop', 10, 75000)
item2 = Inventory('002', 'Smartphone', 20, 30000)
item1.add_item(5)
item1.check_item_details()
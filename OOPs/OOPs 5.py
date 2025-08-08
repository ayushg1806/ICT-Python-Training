class Restaurant():
    def __init__(self):
        self.menu_items = {}
        self.bookings = {}  # <-- changed from list to dict
        self.customer_orders = {}
    
    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price
    
    def book_table(self, customer_name, table_number):
        if customer_name not in self.bookings:
            self.bookings[customer_name] = table_number
            print(f'Table {table_number} booked for {customer_name}.')
        else:
            print(f'{customer_name} already has a booking.')
    
    def customer_order(self, customer_name, order_items):
        if customer_name not in self.customer_orders:
            self.customer_orders[customer_name] = order_items
            print(f'Order placed for {customer_name}: {order_items}')
        else:
            print(f'{customer_name} has already placed an order.')

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f'{item}: ₹{price}')
    
    def display_total(self):
        total = 0
        for order in self.customer_orders.values():
            for item in order:
                if item in self.menu_items:
                    total += self.menu_items[item]
        print(f'Total amount for all orders: ₹{total}')


# Using the class
restaurant = Restaurant()

restaurant.add_item_to_menu('Pizza', 300)
restaurant.add_item_to_menu('Burger', 150)
restaurant.add_item_to_menu('Pasta', 200)

restaurant.display_menu()

restaurant.book_table('Ayush', 5)

restaurant.customer_order('Ayush', ['Pizza', 'Pasta'])

restaurant.display_total()
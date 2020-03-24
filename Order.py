"""print("\nHere is your order summary:")
print(" Date: " + date_of_order)
print(" Product: " + product_name)
print(" Amount: " + quantity)
print(" Category: " + category)
"""


class Order:

    def __init__(self, product_name, date_of_order, quantity, category):
        self.product_name = product_name
        self.date_of_order = date_of_order
        self.quantity = quantity
        self.category = category

    def new_category(self):
        if self.category == "Other":
            return "\n You may create a new category later on."
        else:
            pass

    def see_a_date(self):
        print("The date of order is " + self.date_of_order)

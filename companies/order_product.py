from abc import ABC, abstractmethod

class Node:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ICompany(ABC):
    def __init__(self):
        self.users = []
        self.products = []

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def set_users(self, users):
        pass

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def set_products(self, products):
        pass

    @abstractmethod
    def add_product(self, product, quantity):
        pass

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def make_order(self, products, user):
        pass

class IProduct(ABC):
    def __init__(self, id, name, price, shipping_cost):
        self.id = id
        self.name = name
        self.price = price
        self.shipping_cost = shipping_cost

    @abstractmethod
    def get_id(self):
        pass    

class IUser(ABC):
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
        self.orders = []

    @abstractmethod
    def get_orders(self):
        pass

    @abstractmethod
    def set_orders(self, orders):
        pass

class Product(IProduct):
    def __init__(self, id, name, price, shipping_cost):
        super().__init__(id, name, price, shipping_cost)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_shipping_cost(self):
        return self.shipping_cost

    def set_shipping_cost(self, shipping_cost):
        self.shipping_cost = shipping_cost

class User(IUser):
    def __init__(self, id, name, balance):
        super().__init__(id, name, balance)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_orders(self):
        return self.orders

    def set_orders(self, orders):
        self.orders = orders

class Company(ICompany):
    def __init__(self):
        super().__init__()
        self.users = []
        self.products = []  # list of Node(product, quantity)

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    def add_product(self, product, quantity):
        # Check if product already exists by product id
        for node in self.products:
            if node.product.id == product.id:
                node.quantity += quantity
                return
        # If not found, add new Node
        self.products.append(Node(product, quantity))

    def add_user(self, user):
        self.users.append(user)

    def make_order(self, order_products, user):
        total_cost = 0
        max_shipping = 0

        # Check availability and calculate total cost + max shipping
        for order_node in order_products:
            product_id = order_node.product.id
            quantity = order_node.quantity
            matched_node = next((p for p in self.products if p.product.id == product_id), None)

            if not matched_node:
                print(f"Product ID {product_id} not found")
                return False
            if matched_node.quantity < quantity:
                print(f"Insufficient quantity for product ID {product_id}")
                return False
            
            total_cost += matched_node.product.price * quantity
            max_shipping = max(max_shipping, matched_node.product.shipping_cost)

        total_cost += max_shipping

        if user.balance < total_cost:
            print(f"User {user.name} does not have enough balance")
            return False

        # Deduct quantities and add order nodes to user
        for order_node in order_products:
            product_id = order_node.product.id
            quantity = order_node.quantity
            matched_node = next((p for p in self.products if p.product.id == product_id), None)
            matched_node.quantity -= quantity
            user.orders.append(Node(matched_node.product, quantity))

        user.balance -= total_cost
        return True

if __name__ == "__main__":
    company = Company()

    product_count = int(input().strip())
    for _ in range(product_count):
        a = input().strip().split(",")
        # a[0]: id, a[1]: name, a[2]: price, a[3]: shipping_cost, a[4]: quantity
        company.add_product(Product(int(a[0]), a[1], float(a[2]), float(a[3])), int(a[4]))

    user_count = int(input().strip())
    for _ in range(user_count):
        a = input().strip().split(",")
        # a[0]: id, a[1]: name, a[2]: balance
        company.add_user(User(int(a[0]), a[1], float(a[2])))

    order_count = int(input().strip())
    for _ in range(order_count):
        a = input().strip().split(",")
        user_id = int(a[0])
        user = next((u for u in company.get_users() if u.id == user_id), None)
        if user is None:
            raise Exception(f"User with ID {user_id} not found")

        order_products = []
        for j in range(1, len(a)):
            b = a[j].split("|")
            product_id = int(b[0])
            quantity = int(b[1])
            # Find the product from company's product list
            matched_node = next((p for p in company.get_products() if p.product.id == product_id), None)
            if matched_node is not None:
                order_products.append(Node(matched_node.product, quantity))

        company.make_order(order_products, user)

    # Output all products sorted by product id with updated quantities
    output = sorted(company.get_products(), key=lambda x: x.product.id)
    output = [f"{x.product.name}:{x.quantity}" for x in output]
    print("\n".join(output))

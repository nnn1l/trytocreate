class Product:
    def __init__(self, type_, name, price, amount):
        self.type = type_
        self.name = name
        self.price = price
        self.amount = 0


class ProductStore:
    def __init__(self):
        self.basket = {}
        self.money = 0.0

    def add(self, product: Product, amount: int): # - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
        if not isinstance(product, Product) or amount <= 0:
            raise ValueError("Invalid product or amount.")
        increased_price = 1.3 * product.price
        self.basket[product.name] = {"product" : product}
        self.basket[product.name]["product"].amount += amount

    def set_discount(self, product: Product, identifier, percent): # - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
        if percent <= 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        past_price = product.price * product.amount
        if identifier == (product.name or product.type):
            price_down = past_price * (1 - percent/100)
            self.money += price_down - past_price
        else:
            raise ValueError("No such name or type of products")

    def sell_product(self, product_name, amount: int): # - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
        products_data = self.basket.get(product_name)
        if products_data is not None:
            product_amount = self.basket[product_name]["product"].amount
            if self.basket[product_name]["product"].amount < amount:
                raise ValueError("You are not able to sell more products than you have.")
            else:
                self.money += self.basket[product_name]["product"].price * (amount - product_amount)
                self.basket[product_name]["product"].amount -= amount

    def get_income(self): # - returns amount of many earned by ProductStore instance.
        return self.money

    def get_all_products(self): # - returns information about all available products in the store.
        for key in self.basket.keys():
            print({self.basket[key]})

    def get_product_info(self, product_name): # - returns a tuple with product name and amount of items in the store.
        if product_name not in self.basket:
            raise ValueError("Product not found.")
        return (product_name, self.basket[product_name]["product"].amount)


p = Product('Sport', 'Football T-Shirt', 100, 0)

p2 = Product('Food', 'Ramen', 1.5, 0)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)


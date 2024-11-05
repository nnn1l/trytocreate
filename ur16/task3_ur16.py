class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.basket = {}
        self.money = 0.0

    def add(self, product, amount): # - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
        if not isinstance(product, Product) or amount <= 0:
            raise ValueError("Invalid product or amount.")
        increased_price = 1.3 * product.price
        if product.name in  self.basket.values():
            self.money += amount * increased_price
            self.basket[product.name]['amount'] += amount
        else:
            self.basket[product.name] = {"type": product.type, "amount" : amount, "price": increased_price}

    def set_discount(self, identifier, percent, identifier_type='name'): # - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
        if percent <= 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        for key, value in self.basket.items():
            typing = value['type']
            past_price = value['price']
            if identifier == self.basket[key] or identifier_type == typing:
                price_down = past_price * (1 - percent/100)
                self.basket[key]['price'] = price_down
                self.money += price_down - past_price
            else:
                raise ValueError("No such name or type of products")

    def sell_product(self, product_name, amount): # - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
        if product_name in self.basket.keys():
            if self.basket[product_name]['amount'] < amount:
                raise ValueError("You can`t sell more products that you have.")
            else:
                self.money -= self.basket[product_name]['price'] * (self.basket[product_name]['amount'] - amount)
                self.basket[product_name]['amount'] -= amount
        else:
            raise ValueError("No such name of products")

    def get_income(self): # - returns amount of many earned by ProductStore instance.
        return self.money

    def get_all_products(self): # - returns information about all available products in the store.
        for key in self.basket.keys():
            print(f'{self.basket[key]}  ->  {self.basket[key]["price"]}')

    def get_product_info(self, product_name): # - returns a tuple with product name and amount of items in the store.
        if product_name not in self.basket:
            raise ValueError("Product not found.")
        return (product_name, self.basket[product_name]['amount'])


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)


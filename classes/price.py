class Item():
    def __init__(self,name,price=100,discount=0.05):
        self.name = name
        self.price = price
        self.discount = discount

    def noDiscount(self):
        self.discount = 0

    def checkout(self):
        print("----------")
        print(f'ITEM: {self.name.upper()}')
        print(f'PRICE:  ${self.price: .2f}')
        print(f'DISCOUNT:  {self.discount: .0%}')
        print(f'TOTAL SELLING PRICE:  ${(self.price * self.discount)+self.price: .2f}')

handbag = Item('Louis Vuitton Bag',1400)

handbag.checkout()


## reducing the discount to 0
handbag.noDiscount()
handbag.checkout()

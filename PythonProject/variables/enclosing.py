#E

def cart():
    discount=10000 #E
    bill=discount

    def checkout():
        print("checkout amount is a discount amount : " ,discount)

    def pay():
        print("bill is also discount amount :" ,bill)

    pay()

    checkout()

cart()
amount =1000
tax = amount*0.18
print("Actual amount is ",amount)
print("Tax amount from actual amount ",tax)
total = amount+tax
print("Total amount is along with tax ",total)

if total > 1000 :
    discount = total * 0.10
    total -= discount
    print("Total amount after discount is ",total)
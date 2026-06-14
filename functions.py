def greet(name="guest"):
    print("Hello", name)

greet()
greet("harshita")

def cal_totalbill(rate,quantity):
    total = rate*quantity
    print(total)
    
cal_totalbill(100,5)

bill=cal_totalbill(10,5)
print(bill)

def cal_total_bill(rate, quantity):
    total = rate * quantity
    return total

bill = cal_total_bill(10, 5)
print(bill)
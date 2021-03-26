#expense report 

def sum_of_args(*argv):
    sum = 0
    for number in argv:
        sum = sum + number
    return sum

def product_of_args(*argv):
    product = 1
    for number in argv:
        product = product * number
    return product

expenses = []
with open("day1_input.txt","r") as file:
    for line in file:
        expenses.append(int(line))

n = len(expenses)
for i in range(n):
    for j in range(i+1,n):
        sum_expenses = sum_of_args(expenses[i], expenses[j])
        if(sum_expenses == 2020):
            print(f"{expenses[i]} + {expenses[j]} = {sum_expenses}")
            product_expenses = product_of_args(expenses[i],expenses[j])
            print(f"{expenses[i]} * {expenses[j]} = {product_expenses}")
        for k in range(j+1,n):
                sum_expenses = sum_of_args(expenses[i], expenses[j], expenses[k])
                if(sum_expenses == 2020):
                    print(f"{expenses[i]} + {expenses[j]} + {expenses[k]} = {sum_expenses}")
                    product_expenses = product_of_args(expenses[i],expenses[j], expenses[k])
                    print(f"{expenses[i]} * {expenses[j]} * {expenses[k]} = {product_expenses}")



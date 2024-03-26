from functools import reduce

list1 = [10, 20, 30, 40, 50]

def perfect(num1, num2):
    print("num1 = ",num1,"\t","num2 = ",num2)
    return num1 + num2

total = reduce(perfect, list1)
print(total)
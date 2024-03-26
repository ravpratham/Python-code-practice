'''
1) Instantiate the Cat object with 3 cats

2) Create a function that finds the oldest cat

3) Print out: "The oldest cat is x years old.", where x will be the oldest cat age by using the function in #2
'''
class Cat:
    def __init__(self,age):
        self.cat_age = age

cat1 = Cat(5)
cat2 = Cat(7)
cat3 = Cat(2)

def find_oldest_cat():
    lst = [cat1.cat_age, cat2.cat_age, cat3.cat_age]
    return max(lst)


print(f"The oldest cat is {find_oldest_cat()} years old.")

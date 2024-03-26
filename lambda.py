List = [1,2,3,4,5]
#print(list(map(lambda x: x*x, List)))

cube = lambda num: num * num * num
#print(cube(5))

def apply(fx, x):
    return 6 + fx(x)

#print(apply(cube, 5))

my_list = [5,4,3]
print(list(map(lambda item: item*item, my_list)))


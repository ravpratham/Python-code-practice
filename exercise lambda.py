#List Sorting
#you have to sort the given list on the basis of second index

a = [(0,2), (4,3), (9,9), (10, -1), (10, -2)]

# from operator import itemgetter
# print(sorted(a, key = itemgetter(1)))

a.sort(key = lambda item: item[1])
print(a)
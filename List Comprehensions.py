# my_list1 = [char for char in range(1, 101)]
# my_list2 = [char*2 for char in range(1, 101)]
# my_list3 = [char*char for char in range(1, 101)]
# my_list4 = [char*char for char in range(1, 101) if char % 2 == 0]  # only even numbers will be added to the list

# print(my_list4)
my_list5 = []
for i in "hello":
    my_list5.append(i)
print(my_list5)

my_list6 = [char for char in "hello"]
print(my_list6)


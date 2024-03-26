'''
List = [
    {'name': "Pratham","R num": 21,"DOB": "17/7/2005","grade": "A","attendance": 75},
    {'name': "Ram","R num": 10,"DOB": "12/2/2005","grade": "B","attendance": 50},
    {'name': "Priyanshu","R num": 54,"DOB": "15/5/2005","grade": "C","attendance": 90}
]
List2 = []
#name = input("enter the name of the student - ")
List_names = []
for Dict in List:
    List_names.append(Dict['name'])
    List_names.sort()
    print(List_names)
    for name in List_names:
        if Dict['name'] == name:
            List2.append(Dict)
            print(List2)

#print(List)

c = 3.14
print(c%2.0)
'''

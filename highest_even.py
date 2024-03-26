def highest_even(arr):
    max = 0
    for num in arr:
        if (num%2 == 0) and (num > max):
            max = num
    return max

def max_even(arr):
    new_arr = arr
    while max(new_arr)%2 != 0:
        new_arr.remove(max(new_arr))
    return max(new_arr)

arr = [12,10, 2, 3,15, 4, 8, 11]
print(highest_even(arr))
print(max_even(arr))
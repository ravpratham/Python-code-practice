picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    print()

    for digit in row:
        if digit == 0:
            print(" ", end = '')

        elif digit == 1:
            print("*", end = '')


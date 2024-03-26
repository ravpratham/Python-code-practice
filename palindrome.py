def palindrome(sequence):
    l = str(sequence)
    if len(l)%2!=0:
        n=(len(l)+1)//2
        firsthalf = l[:n]
        secondhalf = l[n-1:]
        if firsthalf == secondhalf[::-1]:
            return True
    else:
        return False

#x = int(input("enter a number - "))

x = 1232
print(palindrome(x))
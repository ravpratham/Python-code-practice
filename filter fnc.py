def triple(pack):
    return pack%2 == 0

pack = [1,1,2,2,3]

print(list(filter(triple, pack)))
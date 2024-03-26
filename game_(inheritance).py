'''
User
 - wizards
 - archers
    all wizards and archers are users (wizards and archers are children classes of user)
    '''

class User():
    def login(self):  # no requirement of innit
                      # nothing to pass an argument
        print("logged in")

class wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def perform(self):
        print(f"{self.name} attacking enemy using the ability {self.power}")
        return self.name


class archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.power = num_arrows

    def perform(self):
        print(f"{self.name} attacking enemy with {self.power} arrows")
        return self.name


wizard1 = wizard('Yoru', 'Decoy')
print(wizard1.perform())
print(wizard1.power)

print()

archer1 = archer('Sova', 50)
print(archer1.perform())
print(archer1.power)



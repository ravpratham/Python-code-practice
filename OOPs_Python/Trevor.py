class GameMan:
    def __init__(self, Tname, Tgun, Tdialect, ):
        self.name = Tname
        self.gun = Tgun
        self.dialect = Tdialect

    def walk(self):
        return self.name + ' can walk'

    def talk(self):
        return self.name + ' can speak ' + self.dialect

    def run(self):
        return self.name + ' can run'

    def jump(self):
        return self.name + ' can jump very high'

    def shoot(self):
        return self.name + ' has ' + self.gun + ' pistol'


pratham = GameMan(Tname="Trevor", Tgun="beretta 9mm", Tdialect="Espanol")
print(pratham.shoot())
print(pratham.jump())
print(pratham.talk())
class Person:
    name = "Arijit"

    @classmethod
    def changeName(self, newName):
        self.name = newName

p = Person()
p.changeName("ArijitDas")
print(p.name)
print(Person.name)
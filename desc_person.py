class Person:
    name = ""
    age = 0
    net_worth = 0

    def description(self):
        person_desc = f"{self.name} is {self.age} years old and has a networth of {self.net_worth} US dollars."
        return person_desc


person1 = Person()
person1.name = "Elon"
person1.age = 50
person1.net_worth = 179

person2 = Person()
person2.name = "jeff"
person2.age = 57
person2.net_worth = 192

print(person1.description())
print(person2.description())

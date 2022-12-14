# الجزء الاول
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"my name is {self.name} and I am {self.age} years old"
    # def is_adult(self):
    #     if self.age > 18:
    #         print("You have too much responsibilities")
    #     elif self.age < 18:
    #         print("Lucky you")


# first_person = Person()
# print(first_person.name)
# print(first_person.age)

# الجزء الثاني
# first_person.is_adult()

# الجزء الثالث
first_person = Person("Humoud", 23)
print(first_person)

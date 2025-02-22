from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        #if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            #age -= 1
        return age

person1 = Person("Raissa", "BURUNDI", date(2005, 10, 25))

print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())

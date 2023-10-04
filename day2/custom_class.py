import numbers


class Employee:
    is_human = True  # similar to static variable of Java, as there are no static variables in PY
    # the static variable should outside the constructor
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        # in the PY constructor we may point out default arguments (in parentheses)
        # to allow us in the implementation part to skip unfilled variables
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self): # instance method
        print(f'{self.name} is working') # f - is for concatenation purpose

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


employee1 = Employee()
# will print only default values as above because we do not put any args here, so it will take default

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel') # only one parameter will be printed and others are default

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Yulia', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

# print(Employee.name) # as it is not static variables we are not able to revoke it by the class name
print(Employee.is_human)
print(Employee.planet)

employee1.work()
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)
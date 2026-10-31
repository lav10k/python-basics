class Employee:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept


class Salary(Employee):
    def __init__(self, id, name, dept, salary):
        Employee.__init__(self, id, name, dept)
        self.salary = salary
        self.pf = salary * 0.20
        self.insurance = salary * 0.40
        self.gross = salary + self.pf + self.insurance

    def display(self):
        print("\nEmployee ID :", self.id)
        print("Name :", self.name)
        print("Department:", self.dept)
        print("Salary :", self.salary)
        print("PF :", self.pf)
        print("Insurance :", self.insurance)
        print("Gross Salary :", self.gross)


n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))
    e = Salary(id, name, dept, salary)
    e.display()
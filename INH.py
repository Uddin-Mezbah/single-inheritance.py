class Employee:
    no_of_leavs = 8

    def __init__(self, aname,asalary,coding):
        self.name = aname
        self.salary = asalary
        self.work = coding

    def printdetails(self):
        return f"The Name is{self.name}.Salary is {self.salary}.work is{self.work}"

    @classmethod
    def change_leaves(cls,newleavs):
        cls.no_of_leavs = newleavs

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("Thid is good " + string)

class coding(Employee):
    no_of_holiday = 56
    def __init__(self,aname,asalary,coding,languages):
        self.name = aname
        self.salary = asalary
        self.coding = coding
        self.languages = languages

    def printcode(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and work is {self.coding}.The languages is {self.languages}"


harry = Employee("Harry", 400, "Instructor")
davide = Employee("davide", 500, "Student")




Mezbah = coding("Mezbah", "10000$", "coding", ["python"])
Uddin = coding("Uddin", 777, "coding", ["python", "Cpp"])
print(Mezbah.printcode())


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")

emp = Employee(1, "Coder")

emp.display()

del emp.id

try:
    print(emp.id)
except Exception as e:
    print("Exception occurred: ", e)
    print("emp.id is not defined")

del emp

try:
    emp.display()
# except NameError:
except Exception as e:
    print("Exception occurred: ", e)
    print("emp is not defined")



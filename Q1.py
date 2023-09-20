employees = dict()
while(True):
    name = input("Employee name: ")
    if name.lower() == "no":
        break
    salary = input("Salary: ")
    employees[name] = salary
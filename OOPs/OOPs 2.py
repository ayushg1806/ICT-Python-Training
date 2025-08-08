#Employee Class with Salary, Department, and Overtime Calculation

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print('Name: ', self.name)
        print('ID: ', self.emp_id)
        print('Salary: ', self.salary)
        print('Department: ', self.department)


employee1 = Employee("Mohit", "E9617", 50000, "Accounting")
employee2 = Employee("Krishna", "E7499", 45000, "Research")

print('Employee Details:')
employee1.print_employee_details()
print()
employee2.print_employee_details()

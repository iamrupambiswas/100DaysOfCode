class Employee:
    def __init__(self, name, employee_id, department, salary, employment_type):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.employment_type = employment_type
        
    def display_info(self):
        """
            Displays information about the employee.
        """
        print(f"Name: {self.name}\nDepartment: {self.department}\nSalary: {self.salary}\nEmployment Type: {self.employment_type}")
        
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, salary):
        super().__init__(name, employee_id, department, salary, employment_type = 'FullTimeEmployee')

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, hours_work):
        self.hourly_rate = 1000
        self.hours_work = hours_work
        salary = self.hourly_rate * self.hours_work
        super().__init__(name, employee_id, department, salary, employment_type = 'PartTimeEmployee')
        
class Intern(Employee):
    def __init__(self, name, employee_id, department):
        salary = 10000
        super().__init__(name, employee_id, department, salary, employment_type = 'Intern')
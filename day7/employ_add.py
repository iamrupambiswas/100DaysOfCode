class Add:
    def __init__(self):
        self.name = None
        self.employ_id = None
        self.department = None
    
    def add_employ(self):
        self.name = input("Enter the name: ")
        self.employ_id = input("Enter the employ ID: ")
        self.department = input("Enter the department: ")
        return self.name, self.employ_id, self.department
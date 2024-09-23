from employee import *
from employ_add import Add

ans = input("Do you want to add an employee (yes/no): ").lower().strip()
if ans == "yes":
    empl = int(input("""Select the employment type: 
                        1. Full Time
                        2. Part Time
                        3. Intern
                        
                        Type the serial number:     """))
    
    add = Add()
    
    if empl == 1:
        name, id, dept = add.add_employ()
        salary = int(input("How much salary you want to give: "))
        fte = FullTimeEmployee(name, id, dept, salary)
        print("Employee added successfully!")
        ans = input("Do you want to see the details? (yes/no)  ").lower().strip()
        if ans == "yes":
            fte.display_info()
    elif empl == 2:
        name, id, dept = add.add_employ()
        hours = int(input("How many hours you want to give: "))
        pte = PartTimeEmployee(name, id, dept, hours)
        print("Employee added successfully!")
        ans = input("Do you want to see the details? (yes/no)  ").lower().strip()
        if ans == "yes":
            pte.display_info()
    elif empl == 3:
        name, id, dept = add.add_employ()
        int = Intern(name, id, dept)
        print("Employee added successfully!")
        ans = input("Do you want to see the details? (yes/no)  ").lower().strip()
        if ans == "yes":
            int.display_info()
    else:
        print("Invalid serial number typed!")
            
else:
    print("No employee added!")
# Write a Program to Get Employee Information and Store Official Information (eid, designation)
class Employee:
    def __init__(self, eid, designation):
        self.eid = eid
        self.designation = designation

    def display_info(self):
        print(f"Employee ID: {self.eid}")
        print(f"Designation: {self.designation}")


# Input Employee Information
eid = input("Enter Employee ID: ")
designation = input("Enter Employee Designation: ")

# Create Employee object and display information
emp = Employee(eid, designation)
emp.display_info()

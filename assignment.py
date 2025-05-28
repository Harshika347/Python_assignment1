class Department:
    count = 0  

    def __init__(self, id, name, place, head):
        self.id = id
        self.name = name
        self.place = place
        self.head = head
        Department.count += 1

    def show_info(self):
        print(f"\nID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.place}")
        print(f"Head: {self.head}")


print("Department Management System")
print("---------------------------")

# creating departments
departments = []
num = int(input("How many departments to add? "))

for i in range(num):
    print(f"\nEnter details for Department {i+1}:")
    d = Department(
        int(input("Enter ID: ")),
        input("Enter Department Name: "),
        input("Enter Location: "),
        input("Enter Head: ")
    )
    departments.append(d)

# all departments
print("\nAll Departments:")
for d in departments:
    d.show_info()

# total count
print(f"\nTotal Departments: {Department.count}")

search_id = int(input("\nEnter ID to search: "))
found = False
for d in departments:
    if d.id == search_id:
        print("\nDepartment Found:")
        d.show_info()
        found = True
        break

if not found:
    print("Department not found!")

search_name = input("\nEnter Department Name to search: ").lower()
found = False
for d in departments:
    if d.name.lower() == search_name:
        print("\nDepartment Found:")
        d.show_info()
        found = True
        break

if not found:
    print("Department not found!")

# output :

# Department Management System
# ---------------------------
# How many departments to add? 3

# Enter details for Department 1:
# Enter ID: 101
# Enter Department Name: CSE
# Enter Location: Block-A
# Enter Head: Harshika

# Enter details for Department 2:
# Enter ID: 102
# Enter Department Name: AIML
# Enter Location: Block-B
# Enter Head: Siri

# Enter details for Department 3:
# Enter ID: 103
# Enter Department Name: ECE
# Enter Location: Block-C
# Enter Head: Harshi     

# All Departments:

# ID: 101
# Name: CSE
# Location: Block-A
# Head: Harshika

# ID: 102
# Name: AIML
# Location: Block-B
# Head: Siri

# ID: 103
# Name: ECE
# Location: Block-C
# Head: Harshi

# Total Departments: 3

# Enter ID to search: 102

# Department Found:

# ID: 102
# Name: AIML
# Location: Block-B
# Head: Siri

# Enter Department Name to search: CSE

# Department Found:

# ID: 101
# Name: CSE
# Location: Block-A
# Head: Harshika



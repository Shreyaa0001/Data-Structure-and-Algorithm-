#Employee IDs are stored as: E201 → E202 → E203 → E204 → E205
#Tasks: Display the employee list. Delete Employee E201 (head node). Display the updated list. Explain how the head pointer changes.
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.next = None
class EmployeeList:
    def __init__(self):
        self.head = None
    def insert(self, emp_id):
        new_employee = Employee(emp_id)
        if self.head is None:
            self.head = new_employee
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_employee
    def delete(self, emp_id):
        if self.head is None:
            print("No employees in the list.")
            return
        if self.head.emp_id == emp_id:
            self.head = self.head.next  # Head pointer changes to the next node
            return
        temp = self.head
        while temp.next:
            if temp.next.emp_id == emp_id:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"Employee {emp_id} not found.")
    def display(self):
        if self.head is None:
            print("No employees in the list.")
            return
        temp = self.head
        while temp:
            print(temp.emp_id, end=" → ")
            temp = temp.next
        print("None")
e = EmployeeList()
e.insert("E201")
e.insert("E202")
e.insert("E203")    
e.insert("E204")
e.insert("E205")

while True:
    choice = input("Enter \n'd' to delete an employee,\n 'v' to view the list, \n 'q' to quit: ")
    if choice == 'd':   
        emp_id = input("Enter the Employee ID to delete: ")
        e.delete(emp_id)
        print(f"Employee {emp_id} deleted")
    elif choice == 'v':
        print("Current list of employees:")
        e.display()
    elif choice == 'q':
        break      
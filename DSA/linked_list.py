# Linked list implementation in Python
class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class LinkedList:    
    def __init__(self):
        self.head = None
    def create(self):    
        n = int(input("Enter the number of nodes: "))
        if n <= 0:
            print("Number of nodes must be greater than 0.")
        for i in range(1,n+1):
            val = input(f"Enter the value for node {i}: ")
            self.insert(val)
    def insert(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
while True:
        print("\nMenu:")
        print("1. Create linked list")
        print("2. Insert node")
        print("3. Display linked list")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            ll.create()
        elif choice == '2':
            val = input("Enter the value for node: ")
            ll.insert(val)
        elif choice == '3':
            ll.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")   

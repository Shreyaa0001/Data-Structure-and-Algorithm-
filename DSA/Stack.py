class Stack:
    def __init__(self):
        self.top = -1
        self.ST=[0]*5
    def insert(self,x):        
        if self.top == 4:
            print("Stack is overflow...")
            return
        self.top = self.top + 1
        self.ST[self.top] = x
    def Delete(self):
        if self.top == -1 :
            print("Stack is underflow...")
            return
        else:
            y = self.ST[self.top]
            self.top = self.top - 1
        return y
    def display(self):
        if self.top == -1:
            print("Nothing to display...")
            return
        for i in range(self.top,-1,-1):
             print(self.ST[i])

s = Stack()
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter the element to be inserted: "))
        s.insert(x)
    elif ch == 2:
        y = s.Delete()
        if y is not None:
            print("Deleted element is:",y)
    elif ch == 3:
        s.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice...")             
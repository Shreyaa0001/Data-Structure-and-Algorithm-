class Stack:
    def __init__(self):
        self.top = -1
        self.ST=[0]*5
    def push(self,x):        
        if self.top == 4:
            print("Stack is overflow...")
            return
        self.top = self.top + 1
        self.ST[self.top] = x
    def pop(self):
        if self.top == -1 :
            print("Stack is underflow...")
            return
        else:
            y = self.ST[self.top]
            self.top = self.top - 1
        return y
    def peek(self):
        if self.top == -1:
            print("Stack is empty...")
            return
        else:
            return self.ST[self.top]
    def display(self):
        if self.top == -1:
            print("Nothing to display...")
            return
        for i in range(self.top,-1,-1):
             print(self.ST[i])

s = Stack()
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter the element to be pushed: "))
        s.push(x)
    elif ch == 2:
        y = s.pop()
        if y is not None:
            print("Popped element is:",y)
    elif ch == 3:
        y = s.peek()
        if y is not None:
            print("Top element is:",y)
    elif ch == 4:
        s.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice...")           

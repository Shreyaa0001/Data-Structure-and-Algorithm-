class Queue:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0]*5
    def insert(self,x):
        if self.R==4:
            print("Queue is overflow...")
            return
        self.R = self.R+1
        self.QT[self.R] = x
        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F== -1:
            print("Queue is underflow...")
            return
        else:
            y = self.QT[self.F]
            if self.F == self.R:
                self.F = -1
                self.R = -1
            else:
                self.F = self.F+1
        return y
    def peek(self):
        if self.F == -1:
            print("Queue is empty...")
            return
        else:
            return self.QT[self.F]
    def display(self):
        if self.F == -1:
            print("Nothing to display...")
            return
        for i in range(self.F,self.R+1):
             print(self.QT[i])
q = Queue()
while True: 
    print("1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter the element to be inserted: "))
        q.insert(x)
    elif ch == 2:
        y = q.delete()
        if y is not None:
            print("Deleted element is:",y)
    elif ch == 3:
        y = q.peek()
        if y is not None:
            print("Front element is:",y)
    elif ch == 4:
        q.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice...")
   

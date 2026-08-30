class History:
    def __init__(self):
        self.top = -1
        self.h = [0]*15
    def push(self,x):    
        if not x.startswith("https://"):
            print("Only URLS strating with https:// are allowed!")
            return
        if self.top == 14:
            print("History is Full!")
            return
        self.top = self.top + 1
        self.h[self.top] = x 
    def pop(self):     
        if self.top == -1 :
            print("No history available!")
            return
        else:
            y = self.h[self.top]
            self.top = self.top - 1
            return y
    def peek(self): 
        if self.top == -1:
            print("History is empty...")
            return
        else:
            return self.h[self.top]    
    def display(self):
        if self.top == -1:
            print("Nothing to display...")
            return
        for i in range(self.top,-1,-1):
             print(self.h[i])  

s = History()        
while True:
    print("1. visit new page")
    print("2. Go back to previous page")
    print("3. Current page")
    print("4. Display History")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = input("Enter URL: ")
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
class BrowsHistory:
    def __init__(self):
        self.current = -1
        self.history = [0]* 15
    
    def visit_new_page(self, page):
        if self.current == 14:
            print("History is full....... Cannot visit new page.....")
            return
        self.current += 1
        self.history[self.current] = page
        
    def go_back(self):
        if self.current == -1:
            print("No previous page to go back to......")
        else:
            print("Going back from:", self.history[self.current])
            self.current -= 1
    
    def current_page(self):
        if self.current == -1:
            print("No current page.")
        else:
            print("Current Page:", self.history[self.current])
    
    def display_history(self):
        if self.current == -1:
            print("History is empty.")
        else:
            print("\nBrowser History (Latest to Oldest):")
            for i in range(self.current, -1, -1):
                print(self.history[i])
h = BrowsHistory()

while True:
    choice = input("\n===== Browser History Menu =====\n1. Visit New Page\n2. Go Back\n3. Current Page\n4. Display Browser History\n5. Exit\nEnter your choice: ")
    if choice == "1":
        page = input("Enter the URL of the new page:") 
        h.visit_new_page(page)
    elif choice == "2":
        h.go_back() 
    elif choice == "3":
        h.current_page()
    elif choice == "4":
        h.display_history() 
    elif choice == "5":
        print("Exiting...")
        break                       
# Browser History using Stack
#Activity2
MAX = 15
history = []


# Visit New Page (Push)
def visit_page():
    url = input("Enter URL: ")

    # Check if URL starts with https://
    if not url.startswith("https://"):
        print("Only URLs starting with https:// are allowed.")
        return

    # Check if history is full
    if len(history) == MAX:
        print("History is full! New page rejected.")
        return

    # Check duplicate consecutive page
    if len(history) > 0 and history[-1] == url:
        print("Same page already visited.")
        return

    history.append(url)
    print("Page visited successfully.")


# Go Back (Pop)
def go_back():
    if len(history) == 0:
        print("No history available.")
    else:
        print("Going back from:", history.pop())


# Current Page (Peek)
def current_page():
    if len(history) == 0:
        print("No current page.")
    else:
        print("Current Page:", history[-1])


# Display Browser History
def display_history():
    if len(history) == 0:
        print("History is empty.")
    else:
        print("\nBrowser History (Latest to Oldest):")
        for page in reversed(history):
            print(page)


# Main Menu
while True:
    print("\n===== Browser History Menu =====")
    print("1. Visit New Page")
    print("2. Go Back")
    print("3. Current Page")
    print("4. Display Browser History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        visit_page()

    elif choice == "2":
        go_back()

    elif choice == "3":
        current_page()

    elif choice == "4":
        display_history()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
        
        
        
        
        
#Activity 5

# Hospital Patient Files using Stack

MAX = 50
stack = []


# Add Patient File (Push)
def add_file():
    if len(stack) == MAX:
        print("Stack is full! Cannot add more files.")
        return

    patient_id = input("Enter Patient ID: ").strip()

    if patient_id == "":
        print("Patient ID cannot be empty.")
        return

    # Check unique Patient ID
    for file in stack:
        if file["id"] == patient_id:
            print("Patient ID already exists.")
            return

    patient_type = input("Enter Patient Type (Emergency/Priority): ").strip().lower()

    if patient_type not in ["emergency", "priority"]:
        print("Only Emergency and Priority patients are allowed.")
        return

    stack.append({
        "id": patient_id,
        "type": patient_type
    })

    print("Patient file added successfully.")


# Review File (Pop)
def review_file():
    if len(stack) == 0:
        print("No files to review.")
    else:
        file = stack.pop()
        print("Reviewed File")
        print("Patient ID:", file["id"])
        print("Patient Type:", file["type"])


# Top File (Peek)
def top_file():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        file = stack[-1]
        print("Top File")
        print("Patient ID:", file["id"])
        print("Patient Type:", file["type"])


# Display File Stack
def display_stack():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("\nPatient File Stack (Top to Bottom)")
        for file in reversed(stack):
            print("Patient ID:", file["id"], "| Type:", file["type"])


# Main Menu
while True:
    print("\n===== Hospital Patient Files =====")
    print("1. Add Patient File")
    print("2. Review File")
    print("3. Top File")
    print("4. Display File Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_file()

    elif choice == "2":
        review_file()

    elif choice == "3":
        top_file()

    elif choice == "4":
        display_stack()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
                
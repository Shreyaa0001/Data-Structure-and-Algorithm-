class Patient:
    def __init__(self):
        self.record = -1
        self.history = [0] * 50

    def is_unique_id(self, patient_id):
        for i in range(self.record + 1):
            existing_file = self.history[i]
            if existing_file and existing_file.get("id") == patient_id:
                return False
        return True
    
    def add_patient_file(self, patient_id, patient_type):
        if self.record == 49:
            print("Patient file stack is full! Cannot add more files.")
            return

        if patient_type not in ["Emergency", "Priority"]:
            print("Warning: Only Emergency and Priority patients are allowed.")
            return

        if not self.is_unique_id(patient_id):
            print("Warning: Patient ID already exists.")
            return

        self.record += 1
        self.history[self.record] = {"id": patient_id, "type": patient_type}
        print("Patient file added successfully.")
    def review_patient_file(self):    
        if self.record == -1:
            print("No files to review.")
        else:
            file = self.history[self.record]
            self.record -= 1
            print("Reviewed File")
            print("Patient ID:", file["id"])
            print("Patient Type:", file["type"])
            
    def top_patient_file(self):
        if self.record == -1:
            print("Stack is empty.")
        else:
            file = self.history[self.record]
            print("Top File")
            print("Patient ID:", file["id"])
            print("Patient Type:", file["type"])
            
    def display_patient_files(self):
        if self.record == -1:
            print("No patient files to display.")
        else:
            print("\nPatient File Stack (Latest to Oldest):")
            for i in range(self.record, -1, -1):
                file = self.history[i]
                print("Patient ID:", file["id"], "| Patient Type:", file["type"])
                
p = Patient()

while True:
    choice = input("\n===== Patient File Management Menu =====\n1. Add Patient File\n2. Review Patient File\n3. Top Patient File\n4. Display Patient Files\n5. Exit\nEnter your choice: ")
    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        patient_type = input("Enter Patient Type (Emergency/Priority): ")
        p.add_patient_file(patient_id, patient_type)
    elif choice == "2":
        p.review_patient_file()
    elif choice == "3":
        p.top_patient_file()
    elif choice == "4":
        p.display_patient_files()
    elif choice == "5":
        print("Exiting...")
        break
                                    
#Case Study 11: Movie Ticket Booking Seat Numbers: 11 → 12 → 13 Tasks: 
# Display booked seats. 
# Insert Seat 14. 
# Delete Seat 12. 
# Display the final list

class Seat:
    def __init__(self, data):
        self.data = data
        self.next = None    
class Booking:
    def __init__(self):
        self.s_no = None
    def insert(self, data):
        new_seat = Seat(data)
        if self.s_no is None:
            self.s_no = new_seat
            return
        temp = self.s_no
        while temp.next:
            temp = temp.next
        temp.next = new_seat
    def delete(self, data):
        if self.s_no is None:
            print("No seats booked.")
            return
        if self.s_no.data == data:
            self.s_no = self.s_no.next
            return
        temp = self.s_no
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"Seat {data} not found.")
    def display(self):
        if self.s_no is None:
            print("No seats booked.")
            return
        temp = self.s_no
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")
s = Booking()
s.insert(11)
s.insert(12)
s.insert(13)
s.delete(12)
s.insert(14)
print("Final list of booked seats:")
s.display()
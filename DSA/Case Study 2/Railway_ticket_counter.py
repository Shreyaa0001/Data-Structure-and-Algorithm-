#Passengers stand in a queue to purchase train tickets. The first passenger in the queue is served first.
#Conditions:The queue can hold a maximum of 50 passengers. Duplicate Ticket IDs are not allowed.
#Only confirmed passengers can join the queue. If the queue is full, no new passenger can enter.
#Operations:Add Passenger (Enqueue)Serve Passenger (Dequeue)View First Passenger (Front) Display Passenger Queue
class Railway_counter:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0]*50
    def add_passenger(self, ticket_id):
        if self.R == 49:
            print("Queue is full. Cannot add new passenger.")
            return
        if ticket_id in self.QT[self.F:self.R+1]:
            print("Duplicate Ticket ID. Cannot add passenger.")
            return
        self.R += 1
        self.QT[self.R] = ticket_id
        if self.F == -1:
            self.F = 0
    def serve_passenger(self):
        if self.F == -1:
            print("Queue is empty. No passenger to serve.")
            return
        served_ticket_id = self.QT[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
        else:
            self.F += 1
        return served_ticket_id
    def view_first_passenger(self):
        if self.F == -1:
            print("Queue is empty. No passenger to view.")
            return
        return self.QT[self.F]
    def display_queue(self):
        if self.F == -1:
            print("Queue is empty. Nothing to display.")
            return
        for i in range(self.F, self.R + 1):
            print(self.QT[i])
            
rc = Railway_counter()
rc.add_passenger(101)
rc.add_passenger(102)   
rc.add_passenger(103)
rc.display_queue()
rc.serve_passenger()
rc.view_first_passenger()            
             
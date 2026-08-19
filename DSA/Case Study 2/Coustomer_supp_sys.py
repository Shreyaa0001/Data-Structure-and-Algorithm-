#Incoming customer support calls are handled in the order they are received.
#Conditions: Queue capacity is 80 calls. Duplicate Call IDs are not allowed. Only active calls are accepted. Queue overflow should be handled.
#Operations: Add Call (Enqueue) Answer Call (Dequeue) View Next Call Display Call Queue
class Customer_support:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0]*80
    def add_call(self, call_id):
        if self.R == 79:
            print("Queue is full. Cannot add new call.")
            return
        if call_id in self.QT[self.F:self.R+1]:
            print("Duplicate Call ID. Cannot add call.")
            return
        self.R += 1
        self.QT[self.R] = call_id
        if self.F == -1:
            self.F = 0
    def answer_call(self):
        if self.F == -1:
            print("Queue is empty. No call to answer.")
            return
        answered_call_id = self.QT[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
        else:
            self.F += 1
        return answered_call_id
    def view_next_call(self):
        if self.F == -1:
            print("Queue is empty. No call to view.")
            return
        return self.QT[self.F]
    def display_queue(self):
        if self.F == -1:
            print("Queue is empty. Nothing to display.")
            return
        for i in range(self.F, self.R + 1):
            print(self.QT[i])
c = Customer_support()
c.add_call(201) 
c.display_queue()
c.answer_call()
c.view_next_call()
c.add_call(202)
c.add_call(203)
c.display_queue()
c.answer_call()
c.view_next_call()
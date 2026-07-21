# Queue Implementation using Array  

queue = [98,234,4658,56,53]
queue.insert(0, 100)
print("Initial Queue:", queue)

queue.insert(0, 200)
print("Queue after Enqueue operation:", queue)

queue.pop()
print("Queue after Dequeue operation:", queue)

queue.pop(3)
print(queue)


# A Ticket booking Counter Serves customers in order they arrive. Implement a Queue using an array to perform: Enqueue, Dequeue, Display operations without using class object.

Queue =[1,2,3,4,5]
print("Initial Queue:", Queue)

print("1.Borrow Ticket\n2.Return Ticket\n3.Display Queue\n4.Exit")
print("Select option to get ticket:")
option = int(input("Enter your option: "))

if 1 == option:
    ticket = int(input("Enter ticket number to borrow: "))
    Queue.append(ticket)
    print("Ticket borrowed successfully.")
    
elif 2 == option:
    if len(Queue)==0:
        print("Queue is empty. No ticket to return.")
    else:   
        returned_ticket = Queue.pop(0)
        print(f"Ticket {returned_ticket} returned successfully.")   
        
elif 3 == option:       
    if len(Queue)==0:
        print("Queue is empty.")
    else:
        print("Current Queue:", Queue)

elif option == 4:
    print("Exiting the program.")            
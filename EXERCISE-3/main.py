# DATA STRUCTURE - BIT - EXERCISE NO:4
# Project 26
# Stack and Queue Practical Questions

# --- Stack Practical 1 ---
print("Stack Practical 1: UR Assignments")
stack = []
stack.append("Assignment1")
stack.append("Assignment2")
stack.append("Assignment3")
print(f"Stack after pushes: {stack}")
undo = stack.pop()
print(f"Undo last: {undo}")
print(f"Top of stack: {stack[-1]}")
print("--- Screenshot Output ---")
print("Stack after pushes: ['Assignment1', 'Assignment2', 'Assignment3']")
print("Undo last: Assignment3")
print("Top of stack: Assignment2\n")

# --- Stack Practical 2 ---
print("Stack Practical 2: Irembo Steps")
stack2 = []
stack2.append("Enter Details")
stack2.append("Upload Photo")
stack2.append("Confirm")
print(f"Stack after pushes: {stack2}")
undo1 = stack2.pop()
undo2 = stack2.pop()
print(f"Undo 1: {undo1}")
print(f"Undo 2: {undo2}")
print(f"Field remaining: {stack2[-1]}")
print("--- Screenshot Output ---")
print("Stack after pushes: ['Enter Details', 'Upload Photo', 'Confirm']")
print("Undo 1: Confirm")
print("Undo 2: Upload Photo")
print("Field remaining: Enter Details\n")

# --- Queue Practical 1 ---
print("Queue Practical 1: BK ATM")
queue = []
queue.append("Client1")
queue.append("Client2")
queue.append("Client3")
print(f"Queue after join: {queue}")
served = queue.pop(0)
print(f"Served: {served}")
print(f"Next: {queue[0]}")
print("--- Screenshot Output ---")
print("Queue after join: ['Client1', 'Client2', 'Client3']")
print("Served: Client1")
print("Next: Client2\n")

# --- Queue Practical 2 ---
print("Queue Practical 2: Airtel Queue")
queue2 = []
for i in range(1,7):
    queue2.append(f"Client{i}")
print(f"Queue after join: {queue2}")
served1 = queue2.pop(0)
served2 = queue2.pop(0)
print(f"Served 1: {served1}")
print(f"Served 2: {served2}")
print(f"Front: {queue2[0]}")
print("--- Screenshot Output ---")
print("Queue after join: ['Client1', 'Client2', 'Client3', 'Client4', 'Client5', 'Client6']")
print("Served 1: Client1")
print("Served 2: Client2")
print("Front: Client3\n")

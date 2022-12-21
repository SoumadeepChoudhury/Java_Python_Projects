class Queue:
    def __init__(self,front=None,rear=None,queue=[]):
        self.front=front
        self.rear=rear
        self.queue=queue

    def isEmpty(self):
        if self.queue==[]:
            return True
        else:
            return False

    def Enqueue(self,item):
        self.queue.append(item)
        if len(self.queue)==1:
            self.front,self.rear=0,0
        else:
            self.front=0
            self.rear=len(self.queue)-1
        print("Item added successfully...")

    def Dequeue(self):
        if self.isEmpty():
            return "Underflow"
        else:
            item=self.queue.pop(0)
        if len(self.queue)==0:
            self.front,self.rear=None,None
        else:
            self.front+=1
        return item

    def Peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.queue[0]

    def Display(self):
        if self.isEmpty():
            print("Queue is Empty...")
        elif len(self.queue)==1:
            print(self.queue[0],"<--front,rear")
        else:
            print(f"Front in queue is at --> {self.front}")
            print(f"Rare in queue is at --> {self.rear}")
            print(f"{self.queue[0]} <-- front")
            for item in range(1,len(self.queue)-1):
                print(item)
            print(f"{self.queue[len(self.queue)-1]} <-- rear")


queue=Queue()
while True:
    print("--"*20)
    choice=int(input("Choose your operation from the following:\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit\nEnter your choice: "))
    if choice==1:
        item=input("Enter item to be enqueued: ")
        queue.Enqueue(item)
    elif choice==2:
        item=queue.Dequeue()
        print(f"{item} is dequeued successfully...")
    elif choice==3:
        item=queue.Peek()
        print(f"{item} is Peeked.")
    elif choice==4:
        queue.Display()
    elif choice==5:
        break
    else:
        print("Invalid choice...")

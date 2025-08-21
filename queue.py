### queue 
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  
        self.front = -1  # Front
        self.rear = -1   # Rear

    def checkQueue(self):
        print(self.queue)
        print(f"Queue size: {len(self.queue)}")
        for x in range(len(self.queue)):
          print(self.queue[x])

    def isEmpty(self):
        if self.front == -1:
            print("Your queue is empty")
        else:
            print("Your queue is not empty")
    
    def isFull(self):
        if self.rear == self.size - 1:
            print("Your queue is full")
        else:
            print("Your queue is not full")
    
    def enqueue(self,value):
      if self.rear == self.size -1:
        print("queue is full")
      elif self.front == -1:
        self.front = 0
        self.rear = 0
        self.queue[self.rear]==value
      else:
        self.rear = self.rear + 1
        self.queue[self.rear]=value

    def dequeue(self):
      if self.rear==-1:
        print("empty queue")
      else:
        value_pop = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:  
          self.front = self.rear = -1
        else:
          self.front += 1  
          return value_pop

      
  
testTestQueue = Queue(10)

testTestQueue.isEmpty()
testTestQueue.isFull()
testTestQueue.enqueue(2)
testTestQueue.enqueue(3)
testTestQueue.enqueue(4)
testTestQueue.checkQueue()




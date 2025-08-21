class test:
  def __init__(self,size):
    self.size=size
    self.stack = [None] * size 
    self.setStackTop = -1  #stack pointer 

  def checkStackpointAndList(self):
    print(self.stack)
    print(len(self.stack))

  def isempty(self):
    if self.setStackTop==-1:
        print("your stack is empty")
    else:
        print("your stack is not empty")
  
  def isFull(self):
    if self.setStackTop == self.size - 1:
        print("your stack is Full")
    else:
        print("your stack is not full") 
  
  def push(self,value):
    if self.setStackTop == self.size - 1:
        print("your stack is Full")
    else:
        self.setStackTop += 1
        self.stack[self.setStackTop] = value
  def pop(self):
    if self.setStackTop == -1:
        print("your stack is empty")
    else:
        self.stack[self.setStackTop] = None
        self.setStackTop -=1 
  

testObjectStack = test(10)
testObjectStack.checkStackpointAndList()
testObjectStack.isempty()
testObjectStack.isFull()
testObjectStack.push(1)
testObjectStack.push(2)
testObjectStack.push(33)
testObjectStack.pop()

testObjectStack.isempty()
testObjectStack.checkStackpointAndList()

if __name__ == "__main__":
    stackSize = int(input("please enter the stack size "))
    stackTest = test(stackSize)
    stackpushelement = int(input("please enter the stack element to push"))
    dict_of_options = {

             1:stackTest.checkStackpointAndList(),
             2:stackTest.isempty(), 
             3:stackTest.isFull(),
             4:stackTest.push(stackpushelement),
             5:stackTest.pop()         
    }



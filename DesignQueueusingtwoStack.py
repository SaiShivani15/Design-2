class MyQueue:

    def __init__(self):
        self.inStack=[]
        self.outStack=[]

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outStack.pop()        

    def peek(self) -> int:
        if len(self.outStack)==0:
            while len(self.inStack)>0:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
    def empty(self) -> bool:
        return len(self.outStack)==0 and len(self.inStack)==0
        
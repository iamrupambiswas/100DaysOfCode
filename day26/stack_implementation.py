class Stack:
    def __init__(self):
        self.values = []
    
    def push(self, value):
        self.values.append(value)
        print(self.values)
    
    def pop(self):
        if not self.is_empty():
            self.values.pop()
            print(self.values)
        else:
            print("Stack is empty.")
    
    def is_empty(self):
        return len(self.values) == 0
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.pop()
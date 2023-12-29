class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        new_stack = deque()
        new_stack.append(x)
        for i in range(len(self.stack)):
            temp = self.stack.popleft()
            new_stack.append(temp)  
        self.stack = new_stack

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
      


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
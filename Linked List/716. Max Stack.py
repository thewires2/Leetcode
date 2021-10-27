class MaxStack:

    def __init__(self):
        self.a=[]

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        z= self.a.pop()
        return z

    def top(self) -> int:
        return self.a[-1]

    def peekMax(self) -> int:
        return max(self.a)

    def popMax(self) -> int:
        k=0
        max_element = self.a[0]
        for i in range(len(self.a)):
            if self.a[i]>=max_element:
                k=i
                max_element=self.a[i]
        return self.a.pop(k)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

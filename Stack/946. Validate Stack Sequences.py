class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [ ]
        k=0
        for i in pushed:
            stack.append(i)
            
            while stack and stack[-1]==popped[k]:
                stack.pop()
                k+=1
        if stack==[]:
            return True

class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        y=[]
        x=[root]
        while x:
            a=x.pop()
            if a:
                if a.left!=None and a.right==None:
                    y.append(a.left.val)
                    x.append(a.left)
                elif a.right!=None and a.left==None:
                    y.append(a.right.val)
                    x.append(a.right)
                else:
                    x.append(a.left)
                    x.append(a.right)
        return y

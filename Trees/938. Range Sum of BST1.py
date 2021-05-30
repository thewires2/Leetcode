class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        y=0
        x=[root]
        while x:
            a=x.pop()
            if a:
                if a.val>= low and a.val<=high:
                    y+=a.val
                    x.append(a.left)
                    x.append(a.right)
                elif a.val<=low:
                    x.append(a.right)
                else:
                    x.append(a.left)
        return y

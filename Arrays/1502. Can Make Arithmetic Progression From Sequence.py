class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l1 = arr[0:(len(arr)-1)]
        l2 = arr[1:]
        diffs = [abs(i-j) for i,j in zip(l1, l2)]
        if len(set(diffs)) == 1:
            return True
        return False

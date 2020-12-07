class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        for i in arr2:
            for _ in range(arr1.count(i)):
                output.append(i)
        for i in sorted(list(set(arr1))):
            if i not in output:
                for _ in range(arr1.count(i)):
                    output.append(i)
        return output

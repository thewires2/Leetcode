class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        # initialize hashmap
        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            # find target piece
            if arr[i] not in mapping:
                return False
            # check target piece
            target_piece = mapping[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True

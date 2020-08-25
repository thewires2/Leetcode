class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        z=''
        flat = [val for sublist in paths for val in sublist] 
        z=set(flat[1::2]).difference(set(flat[0::2]))
        j= "".join([str(s) for s in z])
        return j
        

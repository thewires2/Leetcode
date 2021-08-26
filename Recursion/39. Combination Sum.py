class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def recursion(x,path):
          if not path: path=[]
          if x==0: 
            result.append(tuple(sorted(path)))
            
          for i in candidates:
            if x-i>=0:
              recursion(x-i,path+[i])
        recursion(target,[])
        return list(set(result))
        
              

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix=""
        t=[]
        for i in searchWord:
            prefix+=i
            k=[]
            for z in products:
                if z[:len(prefix)]==prefix:
                    k.append(z)
                if len(k)==3:
                    break
            t.append(k)
        return t
                
            

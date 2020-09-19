class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        x=[]
        for i in range(len(prices)-1):
            c=False
            for j in range(i+1,len(prices)):
                if i<j and prices[j]<=prices[i]:
                    x.append(prices[i]-prices[j])
                    c=True
                    break
            if c==False:
                x.append(prices[i])
        x.append(prices[-1])
        return x

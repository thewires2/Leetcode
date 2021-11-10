class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        def find_factors(num):
            factors=[]
            s=int(pow(num,0.5))
            for i in range(1,s+1):
                if num%i==0:
                    factors.append(i)
            return factors[-1]
        
        num1_factor=find_factors(num+1)
        num2_factor=find_factors(num+2)
        
        min_diff=float('inf')
        out = []
        
        if abs(num1_factor-(num+1)//num1_factor)<min_diff:
            min_diff=abs(num1_factor-(num+1)//num1_factor)
            out=[num1_factor,(num+1)//num1_factor]
        if abs(num2_factor-(num+2)//num2_factor)<min_diff:
            min_diff=abs(num2_factor-(num+2)//num2_factor)
            out=[num2_factor,(num+2)//num2_factor]
                
        return out

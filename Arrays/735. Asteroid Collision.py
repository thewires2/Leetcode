class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        x=[]
        for i in asteroids:
            while x and i<0<x[-1]:
                if x[-1] < -i:
                    x.pop()
                    continue
                elif x[-1] == -i:
                    x.pop()
                break
            else:
                x.append(i)
        return x

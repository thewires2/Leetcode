class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        x=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s=[]
        for i in words:
            t=""
            for j in i:
                t+=x[ord(j)-97]
            s.append(t)
        return len(set(s))
                
                

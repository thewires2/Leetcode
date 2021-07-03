class Codec():
    
    def __init__(self):
        self.x = dict() 
        self.i=0

    def encode(self, longUrl: str) -> str:
        self.x[self.i]=longUrl     
        self.i+=1
        return "http://tinyurl.com/"+str(self.i-1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s=shortUrl.replace("http://tinyurl.com/","")
        return self.x[int(s)]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

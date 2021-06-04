class Codec:
    def encode(self, strs: [str]) -> str:
        if len(strs) == 0: 
            return chr(258)
        return chr(257).join(x for x in strs)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258): 
            return []
        return s.split(chr(257))
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

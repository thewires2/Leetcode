class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        return len({x for i in range(1, len(tiles)+1) for x in permutations(tiles, i)})
        

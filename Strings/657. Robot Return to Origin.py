class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return True
        if moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R"):
            return True

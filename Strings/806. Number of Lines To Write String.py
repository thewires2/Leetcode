class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, width = 1, 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width

class Solution:
    def addDigits(self, num: int) -> int:
        # constant time and space since it is a formula from math , checkout hints from leet code
        return 0 if num == 0 else 1 + (num - 1) % 9

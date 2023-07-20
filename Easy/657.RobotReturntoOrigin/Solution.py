class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 0:
            return True

        map = {
            "U" : (0,1),
            "D" : (0,-1),
            "R" : (1,0),
            "L" : (-1, 0)
        }
        result = [0,0]
        for c in moves:
            x,y = map[c]
            result[0] += x
            result[1] += y
        if result == [0,0]:
            return True
        return False


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
        # print(map)

        min_count = 0

        for key in map:
            count = self.find_min_ops(map[key])
            if count == -1:
                return -1
            min_count += count
        return int(min_count)

    def find_min_ops(self, frequency):
        ops = frequency // 3
        while ops > 0:
            remainder = frequency - (3 * ops)
            if remainder == 0:
                return ops
            elif remainder % 2 == 0:
                return ops + (remainder // 2)
            else:
                ops -= 1
        else:
            if frequency % 2 == 0:
                return frequency // 2
            else:
                return -1

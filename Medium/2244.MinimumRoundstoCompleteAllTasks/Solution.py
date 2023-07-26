class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = {}
        count = 0
        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1
        for task in frequency:
            if frequency[task] == 1:
                return -1 
            count += ceil(frequency[task]/3)
        return count
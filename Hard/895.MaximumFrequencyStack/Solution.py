class FreqStack:

    # Time Complexity - O(N) since we are going through array only once
    # Space Complexity - O(N + M)
    # (where is N total numbers in input array and M is maximum frequency of any element )
    # since we are saving all elements once in different lists with in a map of frequency as keys

    def __init__(self):
        self.max_frequency = 0
        self.stacks = {}
        self.counter_map = {}

    def push(self, val: int) -> None:
        self.counter_map[val] = self.counter_map.get(val, 0) + 1
        frequency = self.counter_map[val]
        if frequency not in self.stacks:
            self.stacks[frequency] = []
        self.stacks[frequency].append(val)
        self.max_frequency = max(self.max_frequency, frequency)

    def pop(self) -> int:
        max_freq_element = self.stacks[self.max_frequency].pop()
        self.counter_map[max_freq_element] -= 1
        if len(self.stacks[self.max_frequency]) == 0:
            self.max_frequency -= 1
        return max_freq_element


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

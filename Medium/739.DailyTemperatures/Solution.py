class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Implementing using the concept of monotonically decreasing stack
        # Time Complexity - O(N) since we are only pushing and popping element only once in inner loop
        # Space Complexity - O(N) for stack and output
        stack = []
        output = [0 for _ in range(len(temperatures))]

        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                last_greater_idx = stack.pop()
                output[last_greater_idx] = idx - last_greater_idx
            stack.append(idx)
        return output

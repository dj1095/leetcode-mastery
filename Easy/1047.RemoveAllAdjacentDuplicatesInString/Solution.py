class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Time complexity - O(N)
        # Space Complexity - O(N) due to stack
        stack = []
        for chr in s:
            if stack and stack[-1] == chr:
                stack.pop()
                continue
            stack.append(chr)
        return "".join(stack)

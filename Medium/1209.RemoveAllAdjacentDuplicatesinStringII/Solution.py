class Solution:
    # Time complexity - O(N)
    # Space Complexity - O(N)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for chr in s:
            if stack and stack[-1][0] == chr:
                stack[-1][1] += 1
            else:
                stack.append([chr, 1])
            if stack[-1][1] == k:
                stack.pop()

        return "".join(ch * num for ch, num in stack)

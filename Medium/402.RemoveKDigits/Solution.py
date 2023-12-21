class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Time complexity - O(N)
        # Space Complexity - O(N) due to stack

        # Approach : Increasing Monotonic stack (pop the peak element while k > 0)
        stack = []
        for chr in num:
            while stack and stack[-1] > chr and k > 0:
                stack.pop()
                k -= 1
            stack.append(chr)
        # remove if any k left
        stack = stack[:-k] if k > 0 else stack
        ans = ''.join(stack).lstrip('0')
        return "0" if ans == "" else ans

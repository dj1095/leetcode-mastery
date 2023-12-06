class Solution:
    # Time Complexity - O(N) - since we are using monotonic stack and we only push and pop element once
    # Space Complexity - O(N) - since we use stack and hashmap and in worst case we push all elements to stack

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great_ele_map = {}
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                next_great_ele_map[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        return [next_great_ele_map.get(num, -1) for num in nums1]

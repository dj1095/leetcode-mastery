class Solution:
    #Time Complexity - O(1)
    #Space Complexity - O(1)
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[1]
        
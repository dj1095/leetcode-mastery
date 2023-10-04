class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = start = 0
        consecutive_T = consecutive_F = 0
        for end in range(len(answerKey)):
            if answerKey[end] == "T":
                consecutive_T += 1
            else:
                consecutive_F += 1

            max_repeat_count = max(consecutive_T , consecutive_F)

            if end - start + 1 - max_repeat_count > k:
                if answerKey[start] == "T":
                    consecutive_T -= 1
                else:
                    consecutive_F -= 1
                start += 1
            result = max(result , end - start + 1)
        return result
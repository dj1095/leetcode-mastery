class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        total_distance = 0
        while mainTank >= 5 and additionalTank > 0:
            mainTank = mainTank - 5 + 1
            additionalTank -= 1
            total_distance += 50
        total_distance += mainTank * 10
        return total_distance
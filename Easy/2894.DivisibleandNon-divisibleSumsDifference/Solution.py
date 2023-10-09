class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_of_n_terms = (n * (n + 1))//2
        sum_of_m_factors = 0
        temp = 1
        while temp * m <= n:
            sum_of_m_factors += temp * m
            temp += 1
        return sum_of_n_terms - 2 * sum_of_m_factors
        
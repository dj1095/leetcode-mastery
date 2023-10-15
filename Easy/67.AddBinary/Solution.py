class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Time Complexity - O(N)
        #Space Complexity - O(N)
        i, j = 0, 0
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = []
        while i < len(a) or j < len(b):
            #convert to int
            _a = int(a[i]) if i < len(a) else 0
            _b = int(b[i]) if j < len(b) else 0
            #sum along with carry
            summ = _a + _b + carry
            #update carry with the sum
            carry = summ // 2
            result.append(str(summ % 2))
            i += 1
            j += 1
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])




        
        
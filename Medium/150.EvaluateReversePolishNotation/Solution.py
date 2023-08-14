class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}

        def getEval(op1,op2,operator):
            op1, op2 = int(op1), int(op2)
            result = 0
            if operator == "+":
                result =  op1 + op2
            elif operator == "-":
                result =  op1 - op2
            elif operator == "/":
                result =  op1/op2
            else:
                result =  op1 * op2
            return int(result)

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = getEval(op1,op2,token)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()

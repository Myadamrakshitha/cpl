class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.isnumeric():
                stack.append(int(i))
            elif i=='C':
                stack.pop()
            elif i=='D':
                top=stack[-1]
                stack.append(2*top)
            elif i=='+':
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
    print(sum(stack))

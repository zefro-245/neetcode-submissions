class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res = 0
        for i in tokens:
            if i not in '*+/-':
                stack.append(int(i))
            elif i=='+':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a+b)
            elif i=='-':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            elif i=='*':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a*b)
            elif i=='/':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(int(b/a))
        return stack[0]

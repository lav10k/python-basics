import re
import operator

OPS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '%': (2, operator.mod),
    '^': (3, operator.pow)
}

def tokenize(expr):
    return re.findall(r'\d+\.\d+|\d+|[()+\-*/%^]', expr)

def to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if re.match(r'^\d+(\.\d+)?$', token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   OPS[token][0] <= OPS.get(stack[-1], (0,))[0]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def evaluate(postfix):
    stack = []

    for token in postfix:
        if re.match(r'^\d+(\.\d+)?$', token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPS[token][1](a, b))

    return stack[0]

expr = input("Enter expression: ").replace(" ", "")

tokens = tokenize(expr)
postfix = to_postfix(tokens)
answer = evaluate(postfix)

print("Result =", answer)
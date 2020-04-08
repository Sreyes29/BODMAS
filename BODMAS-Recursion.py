# Function that evaluates the expression without brackets, i.e only with arithmatic operators
def eval(expression, position):
    result = 0
    reducedexp = ''
    # Finding the first token of the expression along with its position
    token, nextposition = findtoken(expression, position)
    # Finding the second token of the expression along with its position
    ntoken, nnextposition = findtoken(expression, nextposition)
    if ntoken == '?':  # Last token condition
        return token
    # Finding the third token of the expression along with its position
    nntoken, nnnextposition = findtoken(expression, nnextposition)
    if ntoken == '/' or ntoken == '*':
        if ntoken == '/':
            result = int(int(token) / int(nntoken))
        elif ntoken == '*':
            result = int(int(token) * int(nntoken))
        reducedexp = token + ntoken + nntoken
        expression = expression.replace(reducedexp, str(result))
        return eval(expression, position)
    else:
        # The original expression remains in the bottom of the stack with its original token, and evaluation happens in the context of
        # subexp. once the ending condition is reached, subexp gets the value of token (as token is returned from ? condition) and
        # the result is then evaluated. int(token) of the result refers to the first token of the expression.
        subexp = eval(expression, nextposition)
        result = int(token) + int(subexp)
        return result

# Function that finds an appropriate token of the expression and returns values of the form +2, -2, /, *


def findtoken(expression, position):
    token = char = ''
    length = len(expression)
    if length == position:
        return '?', -1  # Condition for end of evaluation
    if expression[position] == '-' or expression[position] == '+':
        token = expression[position]
        while position < length:
            position = position + 1  # If length = position then end of expression has been reached
            if position >= length:
                break
            if expression[position].isdigit():
                token = token + expression[position]
            if expression[position] == '+' or expression[position] == '-' or expression[position] == '/' or expression[position] == '*':
                break
        return token, position

    if expression[position] == '*':
        token = '*'
        return token, position + 1

    if expression[position] == '/':
        token = '/'
        return token, position + 1

    if expression[position].isdigit():
        while position < length:
            if expression[position].isdigit():
                token = token + expression[position]
            if expression[position] == '+' or expression[position] == '-' or expression[position] == '/' or expression[position] == '*':
                break
            position = position + 1
        return token, position

# A function that returns the innermost bracket in the expression (which has highest preference)


def findinnerbracket(expression):
    s1 = subexp = ''
    for char in expression:
        if char != ')':
            s1 = s1 + char
        if char == ')':
            break
    s1 = s1[::-1]
    for char in s1:
        if char != '(':
            subexp = subexp + char
        if char == '(':
            break
    subexp = subexp[::-1]
    return subexp

# A function that completely evaluates the expression with brackets


def evalwithbraacket(expression):
    if '(' not in expression and ')' not in expression:
        return eval(expression, 0)
    else:
        subexp = findinnerbracket(expression)
        solution = eval(subexp, 0)
        expression = expression.replace('(' + subexp + ')', str(solution))
        return evalwithbraacket(expression)


expression = input("Enter your expression: ")
expression = expression.replace(" ", "")
result = evalwithbraacket(expression)
print("Result =", result)

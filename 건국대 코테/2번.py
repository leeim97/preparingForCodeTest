sentences = [
    "So when i die (the [first] i will see in (heaven) is a score list).",
    "[ first in ] ( first out ).",
    "Half Moon tonight (At keast ut us better than no Moon at all].",
    "A rope may from )( a trail in a maze",
    "Have a good day",
    "([(([([])()(())]))])."
]
result = []
for i in sentences:
    stack = []
    print(i)
    for j in i:
        if j=='(' or j=='[' or j=='{':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                temp = stack.pop()
                if temp != '(':
                    stack.append(')')
                    break

        elif j == '}':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                temp = stack.pop()
                if temp != '{':
                    stack.append(')')
                    break
        elif j == ']':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                temp = stack.pop()
                if temp != '[':
                    stack.append(')')
                    break
        print(stack)

    print()
    if len(stack) == 0:
        result.append(True)
    else:
        result.append(False)

print(result)
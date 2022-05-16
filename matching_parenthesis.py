problem = input()

stack = []

for c in range(len(problem)):
    if problem[c] == '(':
        stack.append(c)
    elif problem[c] == ')':
        start_index = stack.pop()
        end_index = c
        print(problem[start_index:end_index + 1])

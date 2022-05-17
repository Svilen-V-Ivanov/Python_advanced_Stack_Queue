lines = int(input())

stack = []

for _ in range(lines):
    command = input().split(' ') # може и [int(x) for x in input().split(' ')

    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2' and stack:
        stack.pop()
    elif command[0] == '3' and stack:
        print(max(stack))
    elif command[0] == '4' and stack:
        print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))

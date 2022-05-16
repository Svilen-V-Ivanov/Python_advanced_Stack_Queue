original_string = input()

stack = []

for a in original_string:
    stack.append(a)

reverse_string = ''

while stack:
    reverse_string += stack.pop()

print(reverse_string)

from collections import deque

line = deque()

while True:
    command = input()

    if command == 'End':
        print(f'{len(line)} people remaining.')
        break
    elif command == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(command)

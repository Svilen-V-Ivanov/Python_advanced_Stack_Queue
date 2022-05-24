from collections import deque

cup_list = deque(int(x) for x in input().split())
copy_cup_list = deque()
bottle_list = deque(int(x) for x in input().split())
wasted_water = 0

for b in cup_list:
    copy_cup_list.append(b)

for cup in copy_cup_list:
    current_cup = cup
    while bottle_list:
        current_bottle = bottle_list.pop()

        if current_bottle >= current_cup:
            cup_list.popleft()
            wasted_water += current_bottle - current_cup
            break
        else:
            current_cup -= current_bottle

if not cup_list:
    print(f"Bottles: {' '.join(str(x) for x in bottle_list)}")
else:
    print(f"Cups: {' '.join(str(x) for x in cup_list)}")
print(f"Wasted litters of water: {wasted_water}")

from collections import deque

number_of_stations = int(input())
pumps = deque()

for _ in range(number_of_stations):
    pumps.append([int(x) for x in input().split()])

for attempt in range(number_of_stations):
    tank = 0
    failed = False
    for petrol, distance in pumps:
        tank = tank + petrol - distance
        if tank < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break


from collections import deque

green_light = int(input())
free_window = int(input())
time = green_light + free_window
counter = time
no_crash = True
car_line = deque()
current_car = deque()
passed_cars = 0

while True:
    if not no_crash:
        break

    command = input()

    if command == 'END':
        break
    elif command != 'green':
        car_line.append(command)
    elif command == 'green' and car_line:
        counter = time
        car_name = car_line.popleft()
        current_car = deque(car_name)

        for _ in range(time):
            counter -= 1
            removed_part = current_car.popleft()

            if counter > free_window:
                if not current_car:
                    passed_cars += 1
                    if car_line:
                        car_name = car_line.popleft()
                        current_car = deque(car_name)
                    else:
                        break
                else:
                    if len(current_car) <= counter:
                        passed_cars += 1
                        if counter - len(current_car) > free_window:
                            if car_line:
                                counter -= len(current_car)
                                car_name = car_line.popleft()
                                current_car = deque(car_name)
                            else:
                                break
                        else:
                            break

                    else:
                        for _ in range(counter):
                            removed_part = current_car.popleft()
                        if current_car:
                            removed_part = current_car.popleft()
                        no_crash = False
                        print('A crash happened!')
                        print(f"{car_name} was hit at {removed_part}.")
                        break

            elif free_window >= counter >= 0:
                if len(current_car) <= counter:
                    passed_cars += 1
                    break
                else:
                    for _ in range(counter):
                        removed_part = current_car.popleft()
                    if current_car:
                        removed_part = current_car.popleft()
                    no_crash = False
                    print('A crash happened!')
                    print(f"{car_name} was hit at {removed_part}.")
                    break

if no_crash:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')

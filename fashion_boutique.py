clothes = [int(x) for x in input().split(' ')]
hanger_capacity = int(input())
current_rack_capacity = hanger_capacity
number_of_hangers = 1

while clothes:
    piece_of_cloth = clothes[-1]

    if piece_of_cloth > current_rack_capacity:
        number_of_hangers += 1
        current_rack_capacity = hanger_capacity
    else:
        current_rack_capacity -= piece_of_cloth
        clothes.pop()

print(number_of_hangers)
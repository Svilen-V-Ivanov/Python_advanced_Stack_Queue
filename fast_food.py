from collections import deque

food_quantity = int(input())
quantity_orders_list = [int(x) for x in input().split(' ')]
quantity_orders = deque(quantity_orders_list)
order_complete = False

for order in quantity_orders_list:
    if order <= food_quantity:
        quantity_orders.popleft()
        food_quantity -= order
        if not quantity_orders:
            order_complete = True

    else:
        break

print(max(quantity_orders_list))

if order_complete:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(str(x) for x in quantity_orders)}')

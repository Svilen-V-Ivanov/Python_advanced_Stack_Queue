from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
reversed_bullets = deque(int(x) for x in input().split(' '))
locks = deque(int(x) for x in input().split(' '))
intelligence_value = int(input())
bullets = deque()
shot_bullets = 0
broken_locks = 0
is_failed = False
has_reloaded = False
total_shots_taken = 0


for b in range(len(reversed_bullets) - 1, -1, -1):
    bullets.append(reversed_bullets[b])

for lock in locks:
    shot_bullets = 0
    for shot in bullets:
        shot_bullets += 1
        total_shots_taken += 1

        if lock >= shot:
            broken_locks += 1
            print('Bang!')
            break
        else:
            print('Ping!')

        if total_shots_taken % gun_barrel == 0 and total_shots_taken != len(reversed_bullets):
            print('Reloading!')
    if shot_bullets == len(bullets) and broken_locks != len(locks):
        is_failed = True
        break
    else:
        for _ in range(shot_bullets):
            bullets.popleft()

    if total_shots_taken % gun_barrel == 0 and bullets:
        print('Reloading!')
    # if shot_bullets % gun_barrel == 0 and bullets:
    # print('Reloading!')

price_bullets = len(reversed_bullets) - len(bullets)
if is_failed:
    print(f"Couldn't get through. Locks left: {len(locks) - broken_locks}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullet_price * price_bullets}")
sequence = list(input())
legend = {
    '(': ')',
    '[': ']',
    '{': '}'
}
start = list()
is_balanced = True

for symbol in sequence:
    if symbol in '([{':
        start.append(symbol)
    elif symbol in ')]}' and start:
        first_symbol = start.pop()

        if legend[first_symbol] != symbol:
            is_balanced = False
            break
    else:
        is_balanced = False

if is_balanced and not start:
    print('YES')
else:
    print('NO')

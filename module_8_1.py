def add_everything_up(a, b):
    try:
        return a + b
    except :
        return (f'{a}+{b}')

print(add_everything_up(1, 2))
print(add_everything_up(1, '2'))
print(add_everything_up(1, '2345'))
print(add_everything_up(1, [2, 3, 4, 5]))
print(add_everything_up(1, (2, 3, 4, 5)))
print(add_everything_up(1, {2, 3, 4, 5}))
print(add_everything_up(1, {2: 1, 3: 1, 4: 1, 5: 1}))

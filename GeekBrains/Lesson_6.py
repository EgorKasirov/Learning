import random
max = 100
min = 0
comp_num = random.randint(min, max)
result = None

while result != '=':
    print(comp_num)
    result = input()
    if result == '<':
        min = comp_num
        comp_num = min + (max-min) // 2
    elif result == '>':
        max = comp_num
        comp_num = max - (max-min) // 2
else:
    print('Компьютер победил!')

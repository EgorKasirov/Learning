import random
max = 100
min = 0
comp_num = random.randint(min, max)
flag = False

while flag != True:
    print(comp_num)
    result = input()
    if result == '=':
        print('Компьютер победил!')
        break
    elif result == '<':
        min = comp_num
        comp_num = min + (max-min) // 2
    elif result == '>':
        max = comp_num
        comp_num = max - (max-min) // 2


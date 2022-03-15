#1 Функция принимает на вход Имя, возраст и город проживания человека и возвращает строку
# def man(name, age, city):
#     return f'{name}, {age} год(а), живет в городе {city}'

# name = input('Ведите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# city = input('Введите ваш город: ')

# print(man(name, age, city))

#2 Функция принимает 3 числа и возвращает наибольшее из них

# def max_number(number_1, number_2, number_3):
#     numbers = [number_1, number_2, number_3]
#     return(max(numbers))

# number_1 = int(input('Введите число 1: '))
# number_2 = int(input('Введите число 2: '))
# number_3 = int(input('Введите число 3: '))

# print(f'Максимальное число из введенных - {max_number(number_1, number_2, number_3)}')

#3 Игра. Атакующий и атакуемый 

def atack(person1, person2):
    def armor_fun(person1, person2):
        return person2['damage'] / person1['armor']
    person1['health'] = person1['health'] - armor_fun(person1, person2)
    return (f'{person2["name"]} атаковал {person1["name"]} и оставил у него {person1["health"]} пунктов жизни')
        



gamers_number = int(input('Введите количество игроков: '))
gamers = []
for i in range(gamers_number):
    name = input(f'Введите имя игрока {i+1}: ')
    health = float(input(f'Введите здоровье игрока {i+1}: '))
    damage = float(input(f'Введите урон игрока {i+1}: '))
    armor = float(input(f'Введите уровень брони игрока {i+1}: '))
    gamers.append({'name':name, 'health':health, 'damage':damage, 'armor':armor})

print(atack(gamers[1-1], gamers[2-1]))


   

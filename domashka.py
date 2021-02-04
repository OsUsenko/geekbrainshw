#Первое домашнее задание:

random_list = [111, 'Str', 12.3, False ]

for elements in random_list:
    print(elements, "тип:", type(elements))
-------------------------------------------------------------------------------------
#Второе ДЗ:

r_list = ["H", "e", "l", "l", "o", "g", "u", "y", "s"]

i = 0
for el in range(int(len(r_list) / 2)):
    r_list[i], r_list[i + 1] = r_list[i + 1], r_list[i]
    i += 2

print(r_list)
-------------------------------------------------------------------------------------
#Третье ДЗ:

s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
m = int(input('Введите число месяца: '))
if m ==1 or m ==2 or m == 12:
    print(s_dict.get(1))
    print(s_list[0])
elif m == 3 or m == 4 or m == 5:
    print(s_dict.get(2))
    print(s_list[1])
elif m == 6 or m == 7 or m == 8:
    print(s_dict.get(3))
    print(s_list[2])
elif m == 9 or m == 10 or m == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
    print('Error: нет такого месяца')
-------------------------------------------------------------------------------------
#Четвертое ДЗ:
my_str = input('Введите строку: ')
my_word = []
num = 1

for el in range(my_str.count('') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f'{num} {my_word [el]}')
        num += 1
    else:
        print(f'{num} {my_word [el] [0:10]}')
        num +=1
 -------------------------------------------------------------------------------------
#Пятое ДЗ:
my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
while num != 111:
    for el in range(len(my_list)):
        if my_list[el] == num:
            my_list.insert(el + 1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[el] > num and my_list[el + 1] < num:
            my_list.insert(el + 1, num)
        print(f'Список: {my_list}')
        exit()
 -------------------------------------------------------------------------------------
#Шестое ДЗ:
Не смог справиться, требуется помощь



       


#           # ЗАДАЧА №1

# a = int(input('Введите число месяца: '))      
# def season(a):    
#     if a == 12 or a == 1 or a == 2:
#         print('зима')
#     elif a == 3 or a == 4 or a == 5:
#         print('весна')
#     elif a == 6 or a == 7 or a == 8:
#         print('лето')
#     elif a == 9 or a == 10 or a == 11:
#         print('осень')
#     else:
#         print('ошибка!!!')
# season(a)




#           # ЗАДАЧА №2
# a = int(input('Сколько рублей хотите вкласть: '))
# years = int(input('на сколько лет: '))
# def bank(a,years):
#     count = 0
#     final_number = a
#     while count < years:
#         num = a / 100
#         num1 = num * 10
#         final_number += num1
#         count += 1
        
#     print(final_number)
#     print(count)

# bank(a,years)




#           # ЗАДАЧА №3
# def lists(list1,list2):
#     sums = sum(list1), sum(list2)
#     a = sum(sums)
#     b = a / 10
#     print(b)

# list1 = (32,44,55,66,43)
# list2 = (21,56,76,90,88)
# lists([32,44,55,66,43],[21,56,76,90,88])




#           # ЗАДАЧА №4
# def zero(number):
#     for i in range(number):
#         print(f'{i+1}: 0')

# a = int(input("Введите число:"))
# zero(a)


    





          # ЗАДАЧА №5
def fifth(list1):
    i = 0
    while i < len(list1):
        if 'A' in list1[i] or 'a' in list1[i] or 'I'in list1[i] or 'i' in list1[i]: 
            list1.remove(list1[i])      
        else:
            i += 1
    
list1 = ['Airplane','Cosplay','Holloween','Apple','Computer']
fifth(list1)
print(list1)






#     доп задании
def is_isogram(word):
    word = word.lower()
    unique_letters = set()
    for letter in word:
        if letter in unique_letters:
            print(False)
        unique_letters.add(letter)
        print(True)


word = input("Напишите слово:")
is_isogram(word)





          # доп ЗАДАЧА №2
def number(num):
    a = n[::-1]
    print(a)

n = input('Введите число:')
number(n)




          # доп ЗАДАЧА №3
def chat_box(a):
    if '?' in a:
        print('Конечно!')
    elif 'ВОТ ТАК!' in a:
        print('Успокойся')
    elif a == '':
        print('Как классно, когда ты молчишь. Продолжай в том же духе!')
    else:
        print('ну и что?')


a = input('Напишите что-нибудь:')
chat_box(a)


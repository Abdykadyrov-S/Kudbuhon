# 1
# it_company = ('Google', 'Amazon','Microsoft')
# it_company = list(it_company)
# it_company.append("‘Tesla’")
# print(it_company)

# 2
# print(it_company[1])

# 3
# it_company = list(it_company)
# it_company[0] = 'Apple'
# print(it_company)

# 4
# print(it_company[0:3])

# 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')

# print(text_tuple.count('Python'))

# 6
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# text_tuple = list(text_tuple)
# del text_tuple[3:9]
# for i in text_tuple:
#     print(i)
# text_tuple.insert(3, 'Python')
# text_tuple.insert(4, 'qwert')
# text_tuple.insert(5, 'asdfgh')
# text_tuple.insert(6, 'ghjk')
# text_tuple.insert(7, 'dgxfgn')
# text_tuple.insert(8, 'hjkk')
# print(text_tuple)

# for i in text_tuple:
#     print(i)


# 7
# list = []
# for i in range(1,100):
#     list.append("qwert")
# print(list)

# 8
# lists = list(range(1,1000))
# print(min(lists))
# print(max(lists))
# print(sum(lists))

# 9
# lists_2 = list(range(1,497))
# for i in lists_2:
#     if i %2 ==0:
#         print(i)

# 10
# while True:
#     a = int(input("Введите первое число :"))
#     b = int(input("Введите второе число :"))
#     c = input("+,-,*,/")

#     if c == "+":
#         print(a+b)
#     elif c == "-":
#         print(a-b)
#     elif c == "*":
#         print(a*b)
#     elif c == "/":
#         print(a/b)
    
# доп
# import random

# def get_user_choice():
#     user_choice = input("Выберите: Камень, Ножницы или Бумага? ").strip().lower()
#     while user_choice not in ["камень", "ножницы", "бумага"]:
#         user_choice = input("Некорректный ввод. Выберите: Камень, Ножницы или Бумага? ").strip().lower()
#     return user_choice

# def get_computer_choice():
#     return random.choice(["камень", "ножницы", "бумага"])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "Ничья"
#     elif (user_choice == "камень" and computer_choice == "ножницы") or \
#          (user_choice == "ножницы" and computer_choice == "бумага") or \
#          (user_choice == "бумага" and computer_choice == "камень"):
#         return "Вы победили!"
#     else:
#         return "Вы проиграли."

# def play_game():
#     attempts = 5
#     while attempts > 0:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
        
#         print(f"Вы выбрали: {user_choice}")
#         print(f"Компьютер выбрал: {computer_choice}")
        
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
        
#         attempts -= 1
#         if attempts > 0:
#             print(f"У вас осталось {attempts} попыток\n")
#         else:
#             print("Игра окончена, у вас осталось 0 попыток")

# if __name__ == "__main__":
#     play_game()


# while True:
#         age = int(input("Введите ваш возраст: "))
#         if age >= 18:
#             print("Доступ разрешен")
#             break
#         else:
#             print("Извините, пользование данным ресурсом только с 18 лет")
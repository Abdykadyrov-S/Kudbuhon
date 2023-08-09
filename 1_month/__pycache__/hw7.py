

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def d(a,b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print('не вводите цифру 0')
d(a,b)




#     2
name = input('Введите свое имя: ')
def names():
    if name == "":
        print('Вы не написали свое имя.Введите свое имя!')
    
names()



#           3
password = input('Введите пароль: ')

if len(password) < 8:
    print('пароль слишком короткий.')
else:
    print(password)


        #   4

def sums():
    try:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число: '))
        c = a +b
        print(c)
    except ValueError:
        print('введите числа!')

sums()



#   5
def sums(*args):
    numbers = sum(args)
    print(numbers)
sums(3,5,4)



# доп задание
def argument(*args):
    a = ", ".join(args)
    print(a)
    
argument('body','banana','potato','tomato')


     
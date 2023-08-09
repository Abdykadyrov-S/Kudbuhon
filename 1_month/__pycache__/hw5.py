          # ЗАДАЧА №1
dictionary_1 = {'a': 300, 'b': 400} 
dictionary_2 = {'c': 500, 'd': 600}

dictionary_1.update(dictionary_2)
print(dictionary_1)




          # ЗАДАЧА №2
numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100} 
num = numbers.values()
for i in num:
    mult = i * 5
    print(mult)






          # ЗАДАЧА №3
student = {'name' : 'Askhat', 'age' : 17}
finalage = student['age'] * 2
print(finalage)

student['age'] *= 2
print(student['age'])




          # ЗАДАЧА №4
student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
student['color'] = 'black'
student['age'] = 16
print(student)



          # ЗАДАЧА №5
student = {'name' : 'Askhat', 'age' : 17}
student.pop('age')
print(student)


          # ЗАДАЧА №6
student = {'name' : 'Askhat'}
student['address'] = 'Западный Анар'
print(student)




          # ЗАДАЧА №7
names = {'name_1' : 'Alisa' , 'name_2' : 'Bekbolot' , 'name_3' : 'Sabina', 'name_4' : 'Akilay'}

sortnames = sorted(names.values())
for name in sortnames:
    print(name)







          # ЗАДАЧА №8
students = {
    "Alisa": 2,
    "Bekbolot": 4,
    "Sabina": 3,
    "Nursultan": 5
}


best_students = max(students.values())
for key, values in students.items():
    if values == best_students:
        print(key)




          # ЗАДАЧА №9
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}

for key, value in dict1.items():
        if key in dict2:
            dict2[key] += value
        else:
            dict2[key] = value
print(dict2)






          # ЗАДАЧА №10

students = [{'name': 'Сабина', 'grades': [4, 5, 3, 4, 5]},
    {'name': 'Алиса', 'grades': [5, 5, 4, 5, 3]},
    {'name': 'Бекболот', 'grades': [3, 3, 2, 4, 3]},
    {'name': 'Анна', 'grades': [5, 4, 4, 5, 5]}
]

for i in students:
    grades = i['grades']
    result = sum(grades) / len(grades)
    print(f"Средняя оценка студента {i['name']}: {result}")




                   


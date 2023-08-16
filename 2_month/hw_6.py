import sqlite3

def create_table():
    conn = sqlite3.connect('car_service.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       brand TEXT,
                       model TEXT,
                       year INTEGER,
                       description TEXT,
                       status TEXT)''')
    
    conn.commit()
    conn.close()

def add_car(brand, model, year, description):
    conn = sqlite3.connect('car_service.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO cars (brand, model, year, description, status)
                      VALUES (?, ?, ?, ?, ?)''', (brand, model, year, description, "In Service"))
    
    conn.commit()
    conn.close()

def update_car(car_id, brand=None, model=None, year=None, description=None, status=None):
    conn = sqlite3.connect('car_service.db')
    cursor = conn.cursor()
    
    update_fields = {}
    
    if brand:
        update_fields['brand'] = brand
    if model:
        update_fields['model'] = model
    if year:
        update_fields['year'] = year
    if description:
        update_fields['description'] = description
    if status:
        update_fields['status'] = status
    
    update_query = ', '.join([f'{key} = ?' for key in update_fields.keys()])
    update_values = tuple(update_fields.values()) + (car_id,)
    
    cursor.execute(f'''UPDATE cars SET {update_query} WHERE id = ?''', update_values)
    
    conn.commit()
    conn.close()

def get_all_cars():
    conn = sqlite3.connect('car_service.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM cars''')
    
    cars = cursor.fetchall()
    
    conn.close()
    
    return cars

def get_ready_cars():
    conn = sqlite3.connect('car_service.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM cars WHERE status = ?''', ("Ready",))
    
    ready_cars = cursor.fetchall()
    
    conn.close()
    
    return ready_cars

def show_menu():
    print("База данных автосервиса")
    print("--------------------")
    print("1. Добавить машину")
    print("2. Обновить машину")
    print("3. Посмотреть все машины")
    print("4. Посмотреть готовые машины")
    print("5. Exit")

def main():
    create_table()
    
    while True:
        show_menu()
        
        choice = input("Введите свой выбор: ")
        
        if choice == "1":
            brand = input("Введите бренд: ")
            model = input("Введите модель: ")
            year = int(input("Введите год: "))
            description = input("Введите описание: ")
            
            add_car(brand, model, year, description)
            
            print("Машина успешно добавлена!")
            print()
        elif choice == "2":
            car_id = int(input("Enter the car ID: "))
            brand = input("Введите бренд: ")
            model = input("Введите модель: ")
            year = input("Введите год: ")
            description = input("Введите описание: ")
            status = input("Введите статус: ")
            
            update_car(car_id, brand=brand, model=model, year=year, description=description, status=status)
            
            print("Автомобиль успешно обновлен!")
            print()
        elif choice == "3":
            cars = get_all_cars()
            
            print("All Cars:")
            for car in cars:
                print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Year: {car[3]}, Description: {car[4]}, Status: {car[5]}")
            print()
        elif choice == "4":
            ready_cars = get_ready_cars()
            
            print("Ready Cars:")
            for car in ready_cars:
                print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Year: {car[3]}, Description: {car[4]}, Status: {car[5]}")
            print()
        elif choice == "5":
            break
        else:
            print("Неверный выбор, пожалуйста попробуйте заново.")
            print()

main()
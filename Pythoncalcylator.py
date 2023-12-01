def calculator():
    prodolzhit = '0'
    while prodolzhit == '0':
        print("Список действий:")
        print("1.Сложение")
        print("2.Вычитание")
        print("3.Умножение")
        print("4.Деление")
        print("5.Возведение в степень")
        print("6.Квадратный корень")
        print("7.Факториал")
        print("8.Синус")
        print("9.Косинус")
        print("10.Тангенс")

        operation = input("Выберите операцию: ")
        
        try:
            operation = int(operation)
        except ValueError:
            print("Ошибка: введите число!")
            continue

        if operation in [1, 2, 3, 4]:
            num1 = input("Введите первое число: ")
            num2 = input("Введите второе число: ")

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print("Ошибка: введите число!")
                continue

            if operation == 1:
                result = num1 + num2
                print("Результат:", result)
            elif operation == 2:
                result = num1 - num2
                print("Результат:", result)
            elif operation == 3:
                result = num1 * num2
                print("Результат:", result)
            elif operation == 4:
                if num2 != 0:
                    result = num1 / num2
                    print("Результат:", result)
                else:
                    print("Ошибка: деление на ноль!")

        elif operation == 5:
            num1 = input("Введите число: ")
            power = input("Введите степень: ")

            try:
                num1 = float(num1)
                power = float(power)
            except ValueError:
                print("Ошибка: введите число!")
                continue

            result = num1 ** power
            print("Результат:", result)

        elif operation == 6:
            num = input("Введите число: ")

            try:
                num = float(num)
            except ValueError:
                print("Ошибка: введите число!")
                continue

            if num >= 0:
                result = math.sqrt(num)
                print("Результат:", result)
            else:
                print("Ошибка: квадратный корень из отрицательного числа!")

        elif operation == 7:
            num = input("Введите число: ")

            try:
                num = int(num)
            except ValueError:
                print("Ошибка: введите целое число!")
                continue

            if num >= 0:
                result = math.factorial(num)
                print("Результат:", result)
            else:
                print("Ошибка: факториал отрицательного числа!")

        elif operation in [8, 9, 10]:
            angle = input("Введите угол в градусах: ")

            try:
                angle = float(angle)
            except ValueError:
                print("Ошибка: введите число!")
                continue

            if operation == 8:
                result = math.sin(math.radians(angle))
                print("Результат:", result)
            elif operation == 9:
                result = math.cos(math.radians(angle))
                print("Результат:", result)
            elif operation == 10:
                result = math.tan(math.radians(angle))
                print("Результат:", result)
        else:
            print("Ошибка: некорректная операция!")
            
calculator()

def calculator():
    while True:
        try:
            task = input("Математичний вираз: ")
            numbers, operators = [], []
            num = ""
            for char in task:
                if char.isdigit():
                    num += char
                else:
                    numbers.append(int(num))
                    num = ""
                    operators.append(char)
            numbers.append(int(num))

            result = numbers[0]
            for i in range(len(operators)):
                if operators[i] == '+':
                    result += numbers[i+1]
                elif operators[i] == '-':
                    result -= numbers[i+1]
                elif operators[i] == '*':
                    result *= numbers[i+1]
                elif operators[i] == '/':
                    result /= numbers[i+1]
            print("Результат:", result)
        except Exception as e:
            print("Помилка:", e)
            print("Перевірте правильність введеного виразу.")
calculator()
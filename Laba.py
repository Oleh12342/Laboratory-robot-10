try:
    with open('text.txt', 'w') as file:
        name = str(input("Запишіть своє прізвище у файл: "))
        file.write("Прізвище: " + name + "\n")

        task = str(input("Запишіть питання на тему програмування Python: "))
        file.write("Питання: " + task + "\n")

    print("Дані успішно записані у файл!")
except Exception as e:
    print(f"Сталася помилка: {e}")
        

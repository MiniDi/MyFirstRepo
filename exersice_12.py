def main():
    num_students = int(input("Введите количество студентов: "))
    students = {}

    for _ in range(num_students):
        data = input("Введите имя студента и его оценки: ").split()
        name = data[0]
        try:
            grades = list(map(int, data[1:]))
        except ValueError:
            print("Оценки должны быть целыми числами.")
            return

        if not grades:
            print("Не введены оценки для студента:", name)
            return

        average = sum(grades) / len(grades)
        students[name] = average

    print("\nРезультаты:")
    for name, avg in students.items():
        print(f"{name}: {round(avg, 1)}")

    best_student = max(students, key=students.get)
    best_average = students[best_student]
    print(f"\nЛучший студент: {best_student} (средний балл {round(best_average, 1)})")


if __name__ == "__main__":
    main()
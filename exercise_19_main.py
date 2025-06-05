from exercise_19 import Circle, Rectangle


if __name__ == "__main__":
    shapes = [
        Circle(3),
        Circle(5),
        Rectangle(2, 4),
        Rectangle(3, 7),
        Rectangle(6, 1)
    ]


for shape in shapes:
    print(f"Площадь фигуры {shape.__class__.__name__}: {shape.area():.2f}")
def main():
    N = int(input("Введите число N: "))
    squares = [x**2 for x in range(1, N + 1) if x % 2 == 0]
    print(squares)

if __name__ == '__main__':
    main()
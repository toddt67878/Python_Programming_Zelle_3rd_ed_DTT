def main():
    print("This program is an experiment.")
    x = eval(input("Enter a number between 0 and 1: "))
    a = x
    b = x
    c = x
    for i in range(100):
        a = 3.9 * a * (1 - a)
        b = 3.9 * b * (b - b * b)
        c = 3.9 * c - 3.9 * c * c
        print("{0:<30.20}{1:<30.20}{2:<30.20}".format(a, b, c))


main()

def main():
     print("Ths program illustrates a chaotic function")
     x = float(input("Enter first number between 0 and 1: "))
     y = float(input("Enter second number between 0 and 1: "))
     z = "input"
     print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x, y, z))
     print("---------------------------")
     for i in range(10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print("{0:>14.6f}{1:>13.6f}".format(x, y))


main()

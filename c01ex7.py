def main():
     print("Ths program illustrates a chaotic function")
     x, y = eval(input(
         "Enter 2 numbers between 0 and 1 separated by a comma: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range(10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print(x, "   ", y)


main()

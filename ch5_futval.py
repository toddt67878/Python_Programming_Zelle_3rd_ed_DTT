def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: ", end="/n"))

    print("{0:<9}{1:<7}".format(Year, Value)  # not right

          for i in range(10):
          principal=principal * (1 + apr)
          print("{0:>6}{$1:>8.2f}".format(i, principal))  # not right

          print("The value in 10 years is:", principal)

          main()

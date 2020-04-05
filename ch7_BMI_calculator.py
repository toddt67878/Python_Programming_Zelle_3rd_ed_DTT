def main():
    print("BMI calculator \n")
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))
    bmi = weight * 720 / height
    print = ("Your BMI is ", bmi".")
    if bmi < 19:
        print("You are below the healthy range.")
    elif bmi <= 25:
        print("You are in the healthy range.")
    else:
        print("You are above the healthy range.")


if __name__ == '__main__':
    main()

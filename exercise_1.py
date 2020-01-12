from datetime import datetime


def exercise_1():
    print("Hello, please enter your name and age\n")
    name = input("Please enter your name:\n")
    age = int(input("Please enter your age:\n"))
    age_until_100 = int(100 - age)
    current_year = datetime.today().year
    response = ("Hello " + name + ", you will turn 100 years old in the year " + str(
        current_year + age_until_100) + "\n")
    print(response)
    repeat = int(input("How many times would you like me to repeat this message?\n"))
    for num in range(repeat):
        print(response)


def main():
    exercise_1()


if __name__ == '__main__':
    main()
    print("Thank you for using my program, have a nice day.")

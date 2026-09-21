# Match-Case : Alternate way to using many  elif statements.
# Execute some code if a value matches a case.
# Benefits : Cleaner and more readable.


day = int(input("Enter number of the day: "))


def day_of_the_week(day):
    match day:
        case 1:
            print("Its Monday")
        case 2:
            print("Its Tuesday")
        case 3:
            print("Its Wednesday")
        case 4:
            print("Its Thursday")
        case 5:
            print("Its friday")
        case 6:
            print("Its Saturday")
        case 7:
            print("Its Sunday")
        case _:
            print("Not a day")

print(day_of_the_week(day))
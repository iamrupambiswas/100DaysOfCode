try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution complete!")
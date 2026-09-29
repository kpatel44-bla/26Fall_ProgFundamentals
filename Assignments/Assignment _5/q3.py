#question 3
# number check using given function if it is even or odd.
def check_number(number):       #def takes a number and check if it is even or odd.
    if number % 2 == 0:          #using if else conditionthe number is divisible by 2 then it is even.
        return "Even"            #returning even if the number is even.
    else:
        return "Odd"             #returning odd if the number is odd.

#asking the user to enter a number using input function.
number = int(input("Enter a whole number: "))      #taking only whole numberand asking user to inpuut

#calculationg the result by calling the function and storing the returned value in result variable.
result = check_number(number)
print(f"{number} is an {result} number.")


#question 2
#rectangle calculation function.
#to calculaate the are and perimeter of the rectangle.

def rectangle_stats(length, width): #def takes length and width and calculate the area and perimeter.
    area = length * width #area calculation
    perimeter = 2 * (length + width) #perimeter calculation
    return area, perimeter #returning the area and perimeter enter by the user.

#asking the user to enter the length and width using inputr function.
length = float(input("Enter the length: ")) #taking length input from user
width = float(input("Enter the width: ")) #taking width input from user

#now  calling the function and storing the returned values in area and perimeter variables.
area, perimeter = rectangle_stats(length, width)

#printing the area and perimeter of the rectangle to 2 decimals using float function.
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
 
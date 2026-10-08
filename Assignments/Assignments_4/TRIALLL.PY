#FROM PREVIOUS ASSIGNMENT .
import time
from hs3003 import HS3003

# Set up the HS3003 sensor
# This does NOT read the sensor
sensor = HS3003()


# Function to read and display temperature using board
def temperature():
    t1, h1 = sensor.read()# The sensor is read only when this function is called
    print("Temperature:", t1)


# Function to read and display humidity using board
def humidity():
    t1, h1 = sensor.read()# The sensor is read only when this function is called
    print("Humidity:", h1)


# Display OR  print the menu to be selected by the user.
print("Please choose from the following options:")
print("T - Temperature")
print("H - Humidity")
print("0 - Both")

for i in range(100):# Wait for the user to enter a valid choice using for i .

    choice = input("Enter your choice: ")

    # If T is entered, it will read and display the current temperature
    if choice == "T":
        temperature()
        

    # If H is entered,it will read and display the current humidity
    if choice == "H":
        humidity()
        
    if choice == "0":# If 0 is entered, it will read and display both the current temperature and humidity.
        temperature()
        humidity()

    # If none of the choices above were entered it will ask the usre to enter at least any choice among given or it will show invalid choice.
    else:
        print("Invalid choice. Please enter T, H, or 0.")
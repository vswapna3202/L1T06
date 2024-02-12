# This program inputs numbers until user enters -1 and finds the average of all the numbers entered
# and displays the average

# Input the number from user
input_number = int(input("Please enter a number (-1 to Exit):  "))

# Declare total and count variables to 0
total = 0
count = 0

# Loop through until input entered by user is not -1 which means the loop needs to exit
while (input_number != -1):
# total is sum of all input numbers entered by user add the number to total every time user enters 
# a number
    total += input_number
# count is count of number of numbers entered by user needed to calculate average
    count += 1
# get input number from user again until user enters -1
    input_number = int(input("Please enter a number (-1 to Exit): "))
# loop finishes

# if count is not zero that is if user has entered atleast one number. This is needed as otherwise
# divide by zero error would occur when user has not entered any number and directly entered -1
if (count != 0):
# calculate average by dividing total which is total of all numbers entered by user divided by count
# which is count of numbers entered by user. Display the calculated average to the console
    average = total / count
    print(f"Average of all numbers entered is : {average}")
else:
# if count is 0 it means user did not enter any number so print message Average was not calculated
    print("Average not calculated as no number was entered")

#run with "python3 no_error_handling.py"
#developed for Python 3.6.8 on OSU Flip servers

val = input("Please enter a valid Year: ")

num = int(val)


#Years that are evenly divisible by 4 
# exceptyears that are evenly divisible by 100
# unless the years are also evenly divisible by 400”.
if(num % 400 == 0):
    print(str(num) + " is a leap year!")
elif(num % 100 == 0):
    print(str(num) + " is not a leap year!")
elif(num % 4 == 0):
    print(str(num) + " is a leap year!")
else:
    print(str(num) + " is not a leap year!")
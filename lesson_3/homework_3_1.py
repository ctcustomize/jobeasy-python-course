# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = 10
second_number = 15
results_1 = print
if results_1:
    if first_number > second_number:
        print(first_number)
    else:
        print(second_number)

# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = 21

if number_1 >= 20:
    print('Too high')
else:
    print('Thank you')



# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = 'eric'
last_name = 'Zhan'

if len(first_name) < 5:
    print((first_name + last_name).upper())
else:
    print(first_name.lower())

# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = 21

if 10 < number_2 < 20:
    print('Thank you')
else:
    print('Incorrect answer')

# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 17

if age >= 18:
    print('You can vote')
elif age == 17 :
    print('You can learn to drive')
elif age == 16 :
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-or-Treating')




# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = 12
if month == 1 :
    print('Jan')
elif month == 2 :
    print('Feb')
elif month == 3 :
    print('Mar')
elif month == 4 :
    print('Apr')
elif month == 5 :
    print('May')
elif month == 6 :
    print('Jun')
elif month == 7 :
    print('Jul')
elif month == 8 :
    print('Aug')
elif month == 9 :
    print('Sep')
elif month == 10 :
    print('Oct')
elif month == 11 :
    print('Nov')
elif month == 12 :
    print('Dec')


# ------------------------------------------------------------
# this is file number 9 from el zero assignments
# thos is week 6 from mastering python from el zero web school
# this week about if, elif and else
# it about control flow and make ways in the program
#  ------------------------------------------------------------
print('-' * 50)
num1 = int(input('Enter A Number: ').strip())
num2 = int(input('Enter other Number: ').strip())

operation = input(
    'What Operation You want? "+" Or "-" Or "*" Or "/" Or "%" ').strip()
if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)

elif operation == '/':
    print(num1 / num2)

elif operation == '%':
    print(num1 % num2)

else:
    print('Wrong Operation.')

print('-' * 50)

age = 21
print('App Is Suitable For You'if age > 16 else 'App Is Not Suitable For You')

print('-' * 50)

age = int(input('Enter Your Age: ').strip())
if 100 > age and age > 10:
    days = age * 365.25
    monthes = days / 30
    weeks = days / 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(
        f'You lived {age} Years.\nI Mean {monthes} Monthes.\nI Mean {weeks} Weeks.\nI Mean {days} Days.')
    print(
        f'I Mean {hours} Hours.\nI Mean {minutes} Minutes.\nI Mean {seconds} Seconds.')
else:
    print('age out of range.')

print('-' * 50)

country = input("Enter Your Country: ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(
        f'Your Country Is {country} So You Are Eligible For Discount And The Price After Discount Is $70')
else:
    print(
        f'Your Country Is {country} So You Are Not Eligible For Discount And The Price Is $100')

# ---------------------------------------------------------
# hello, this is el_zero assignment 6 i think
# yesterday i did not watch any video from this coures
# and i was working on web scrabing project to my portfilo
# ---------------------------------------------------------
name = input('Enter your name: ').capitalize().strip()
# Needed Output
print(f'"Hello {name}, Happy To See You Here."')

print('-' * 50)

age = int(input('Enter Your age: '))
if age < 16:
    print('Hello Your Age Is Under 16, Some Articles Is Not Suitable For You')
elif age > 16:
    print(f'Hello Your Age Is {age}, All Articles Is Suitable For You')

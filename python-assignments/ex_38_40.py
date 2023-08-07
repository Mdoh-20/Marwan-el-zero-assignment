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

print('-' * 50)

fname = input('Enter Your First Name: ').strip().capitalize()
sname = input('Enter Your Second  Name: ').strip().capitalize()

print(f"Hello {fname} {sname:.1s}.")

print('-' * 50)

email = input('Enter Your Email: ').strip().lower()


print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(
    f"Email Service Provider Is {email[email.index('@') +1:email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.') +1:]}")

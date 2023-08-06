# ---------------------------------------------------------
# hello, this is el_zero assignment 5 i think
# yesterday i did not watch any video from this coures
# and i was working on web scrabing project to my portfilo
# ---------------------------------------------------------

# True
print(bool(1))
print(bool('Marwan'))
print(bool(['python', 'django', 'flask']))
print(bool({'1-2-2002'}))

print('-' * 50)  # False

print(bool(0))
print(bool(''))
print(bool([]))
print(bool({}))

print('-' * 50)

html = 80
css = 60
javascript = 70

# Needed Output
print(html >= 50 and css >= 50 and javascript >= 50)

print('-' * 50)

num_one = 10
num_two = 20
num = 20

# Needed Output

print(num > num_one or num > num_two)  # True
print(num > num_one and num > num_two)  # False

print('-' * 50)

num_one = 10
num_two = 20
result = num_one + num_two
# Needed Output

print(result)  # 30
print(result ** 3)  # 27000
print((result ** 3) % 26000)  # 1000
print(((result ** 3) % 26000) / 5)  # 200.0
print(type(((result ** 3) % 26000) / 5))  # 200.0
print(type(str(((result ** 3) % 26000) / 5)))  # <class 'str'>

print('-' * 50)

#  that is it

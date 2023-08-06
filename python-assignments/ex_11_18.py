# -----------------------------------------------
# hello, this is assignments number 2
# this assignments about string and string format
# and this is day 2 from el_zero python course
# -----------------------------------------------
myName = 'Marwan'
age = 21
country = 'Egypt'
print(
    f'''"Hello '{myName}', How You Doing \ """ Your Age Is "{age}"" + And Your Country Is: {country}''')

print(f'''"Hello '{myName}', How You Doing \\
""" Your Age Is "{age}"" + 
And Your Country Is: {country}''')

name = 'Elzero'
print(f'{name[1]}\n{name[2]}\n{name[-1]}')

print(f'{name[1:4]}\n{name[::2]}\n{name[-2::-2]}')
# Needed Output
# "lze"
# "Ezr"
# "rzE"

name = "#@#@Elzero#@#@"
print(f'{name.strip("#@")}')
# Needed Output
# Elzero

num = ["9", "15", "130", "950", "1500"]
for i in num:
    print(f'{i.zfill(4)}')
# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

name_one = "Osama"
name_two = "Osama_Elzero"
print(f'{name_one.rjust(20,"@")}')
print(f'{name_two.rjust(20,"@")}')
# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

name_one = "OSamA"
name_two = "osaMA"
print(f'{name_one.swapcase()}')
print(f'{name_two.swapcase()}')
# Needed Output
# osAMa
# OSAma

msg = "I Love Python And Although Love Elzero Web School"
print(f'{msg.count("Love")}')
# Needed Output
# 2


name = "Elzero"
print(f'{name.find("z")}')
# Needed Output
# 2

msg = "I <3 Python And Although <3 Elzero Web School"
print(f'{msg.replace("<3", "love", 1)}')
# Needed Output
# I Love Python And Although <3 Elzero Web School

msg = "I <3 Python And Although <3 Elzero Web School"
print(f'{msg.replace("<3", "love")}')
# Needed Output
# I Love Python And Although Love Elzero Web School

name = "Marwan"
age = 21
country = "Egypt"
print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}.')
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

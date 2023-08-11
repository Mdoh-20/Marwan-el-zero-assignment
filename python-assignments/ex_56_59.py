# ------------------------------------------------------
# This Is Week 8 Assginment [0] From El Zero Web School
# This Assginment About functions and return
# I Don't Study This course Yesterday So
# This Is Day 11 Or 12 For me In El Zero Web School
# I Hope I Can Make This Progress Far Awey From Her
# ------------------------------------------------------


def calculate(num1, num2, ope='add'):
    if ope.lower() == 'add' or ope[0].lower() == 'a':
        num = num1 + num2
        return num
    elif ope.lower() == 'subtract' or ope[0].lower() == 's':
        num = num1 - num2
        return num
    elif ope.lower() == 'multiply' or ope[0].lower() == 'm':
        num = num1 * num2
        return num
    else:
        return 'There Is No Operation Name Like This'


print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30

print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10

print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200


def addition(*numbers):
    count = 0
    for number in numbers:
        if number != 10:
            if number == 5:
                count -= number
                continue
            count += number
    return count


print(addition(10, 20, 30, 10, 15))  # 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # 160


def show_skills(name, *skills):
    if len(skills) > 1:
        print(f'Hello {name} Your Skills Is')
        for skill in skills:
            print(f'- {skill}')
    else:
        print(f'Hello {name} You Have No Skills To Show')


show_skills("Marwan", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")


def say_hello(name='Unknown', age='Unknown', country='Unknown'):
    return f'Hello {name} Your Age Is {age} And You Live In {country}'


print(say_hello("Osama", 38, "Egypt"))  # type: ignore
print(say_hello())

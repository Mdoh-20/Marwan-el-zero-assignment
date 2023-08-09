# ------------------------------------------------------
# This Is Week 7 Assginment [0] From El Zero Web School
# This Assginment About loops Spasifcly while Loop
# This Is About Day 8 Or 9 For me In El Zero Web School
# I Hope I Can Make This Progress Far Awey From Her
# ------------------------------------------------------

while True:
    num = int(input('Enter A Number More Than 0: '))
    if num > 0:
        break
    print(f'Number {num} Is Not More Then 0')
number = num
while num > 0:
    num -= 1
    if num != 6 and num != 0:
        print(num)
else:
    print(f"{number - 1 if number < 6 else number - 2} Numbers Printed Successfully.")

print('-' * 50)

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
lst = []
number = 0
while number < len(friends):
    if friends[number].islower():
        lst.append(friends[number])
    number += 1
    if len(lst) <= 2:
        break
lst = []
num = 0
while num < len(friends):
    if not friends[num].islower():
        print(friends[num])
    else:
        lst.append(friends[num])
    num += 1
print(f'Friends Printed, And Ignored Names Count Is {len(lst)}')

print('-' * 50)

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
num = 0
while len(skills) > num:
    print(skills[num])
    num += 1

print('-' * 50)

num = 0
myFriends = []
while len(myFriends) < 4:
    name = input('Enter A Friend Name: ').strip()
    if not name.isupper():
        myFriends.append(name.capitalize())
        # "Friend osama Added => 1st Letter Become Capital"
        print(f'Friend {name} Added => 1st Letter Become Capital')
        # "Names Left in List Is 3"
        print(f'Names Left in List Is {4 - len(myFriends)}')
    else:
        print('Not Valid Name.')

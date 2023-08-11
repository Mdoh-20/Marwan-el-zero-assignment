# ------------------------------------------------------
# This Is Week 7 Assginment [1] From El Zero Web School
# This Assginment About loops Spasifcly for Loop
# This Is About Day 8 Or 9 For me In El Zero Web School
# I Hope I Can Make This Progress Far Awey From Her
# ------------------------------------------------------

my_nums = [15, 81, 5, 17, 20, 21, 13]
my_sorted_nums = my_nums.sort(reverse=True)
num = 1
for i in my_nums:
    if i % 5 == 0:
        print(f'{num} => {i}')
else:
    print('All Numbers Printed')

print('-' * 50)

for i in range(1, 21):
    if i == 6 or i == 8 or i == 12:
        continue
    print(str(i).zfill(2))
print('All Numbers Printed')

print('-' * 50)

my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
point = 0
points = 0

for key, value in my_ranks.items():
    if value == 'A':
        point = 100
    elif value == 'B':
        point = 80
    elif value == 'C':
        point = 40
    print(
        f'My Rank in {key} Is {value} And This Equal {point} Points')
    points += point
print(f'Total Points Is {points}')

print('-' * 50)

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

for key, value1 in students.items():
    points = 0
    print("------------------------------")
    print(f"-- Student Name => {key}")
    print("------------------------------")
    for chaild_key, chaild_value in value1.items():
        if chaild_value == 'A':
            point = 100
        elif chaild_value == 'B':
            point = 80
        elif chaild_value == 'C':
            point = 40
        elif chaild_value == 'D':
            point = 20
        print(f'{chaild_key} => {point}')
        points += point
    print(f'Total Points For {key} Is {points}')
for student in students:
    points = 0
    print("------------------------------")
    print(f"-- Student Name => {student}---")
    print("------------------------------")
    for sub in students[student]:
        if students[student][sub] == 'A':
            point = 100
        elif students[student][sub] == 'B':
            point = 80
        elif students[student][sub] == 'C':
            point = 40
        elif students[student][sub] == 'D':
            point = 20
        print(f'{sub} => {point}')
        points += point
    print(f'Total Points For {student} Is {points}')

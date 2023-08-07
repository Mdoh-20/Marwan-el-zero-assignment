# --------------------
# this is assignment 4
# --------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
print(f'{friends[0]}')  # "Osama" => Method One
print(f'{friends[-5]}')  # "Osama" => Method Two
print(f'{friends[4]}')  # "Mahmoud" => Method One
print(f'{friends[-1]}')  # "Mahmoud" => Method Two

# Needed Output
print(f'{friends[::2]}')  # "Osama", "Sayed", "Mahmoud"
print(f'{friends[1::2]}')  # "Ahmed", "Ali"

# Needed Output
print(f'{friends[1:4]}')  # "Ahmed", "Sayed", "Ali",
print(f'{friends[3:]}')  # "Ali", "Mahmoud"

# Needed Output
friends[3], friends[4] = 'Elzero', 'Elzero'
print(f'{friends}')  # ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# Needed Output
friends.remove("Nasser")
friends.remove("Osama")
print(friends)  # ["Ahmed", "Sayed", "Salem"]
friends.remove("Salem")
print(friends)  # ["Ahmed", "Sayed"]

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
# Needed Output
friends.extend(employees)
friends.extend(school)
print(friends)  # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
friends.sort()
print(friends)  # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
friends.sort(reverse=True)
print(friends)  # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

# Needed Output
print(len(friends))  # 6

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# Needed Output
print(technologies[-1][0])  # Django
print(technologies[-1][-1])  # Web

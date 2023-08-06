# ----------------------------------------------------
# this is assignment num 5 from el zero python course
# ----------------------------------------------------

# Needed Output
myTuple = 'Marwan',
print(myTuple) # "Osama"
print(type(myTuple)) # <class 'tuple'>

friends = ("Osama", "Ahmed", "Sayed")
lst = list(friends)
lst[0] = 'Elzero'
friends = lst
# Needed Output
print(friends) # ("Elzero", "Ahmed", "Sayed")
print(type(friends)) # <class 'tuple'>
print(len(friends)) # 3 Elements

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

print(nums + letters) # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
print(len(nums + letters))# 6 Elements

my_tuple = (1, 2, 3, 4)

# Needed Output
a , b ,_ ,c = my_tuple
print(a , b ,c)
# 1
# 2
# 4
# --------------------------------------------------------------------------
# this is day four from el zero python course
# i hape i can go to the whole course as a pland and in the time i palnd to
# --------------------------------------------------------------------------

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)

# Needed Output
print(unique_list)  # 1, 2, 3, 4, 5
print(type(unique_list))  # <class 'list'>
print(unique_list[0:4])  # 1, 2, 3, 4

print('-'*50)
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output
all = nums | letters
print(nums | letters)  # {1, 2, 3, "A", "B", "C"}
print(all)  # {1, 2, 3, "A", "B", "C"}
print(nums.union(letters))  # {1, 2, 3, "A", "B", "C"}

print('-'*50)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

print(my_set)  # {1, 2, 3}
my_set.clear()
print(my_set)  # set()
my_set.add('A')  # type: ignore
my_set.add('B')  # type: ignore
print(my_set)  # ("C") {"A", "B"}
my_set.discard("C")  # type: ignore

print('-'*50)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
print(set_one.issubset(set_two))  # True

print('-'*50)

my_dict = {
    'one': {
        'name': 'HTML',
        'Progress': '25%'
    },
    'two': {
        'name': 'CSS',
        'Progress': '0%'
    },
    'three': {
        'name': 'js',
        'Progress': '1%'
    }
}  # Create Dictionary Here

# Needed Output
print(my_dict)
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
my_dict = {
    'four': {
        'name': 'node.js',
        'Progress': '0%'
    }
}
print('-'*50)
print(my_dict['four'])  # "AI Progress Is 20%"

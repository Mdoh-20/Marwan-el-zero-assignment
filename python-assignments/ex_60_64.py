# ------------------------------------------------------
# This Is Week 8 Assginment [1] From El Zero Web School
# This Assginment About functions and return
# I Don't Study This course Yesterday So
# This Is Day 11 Or 12 For me In El Zero Web School
# I Hope I Can Make This Progress Far Awey From Her
# ------------------------------------------------------

def get_score(**subs):
    for sub_key, sub_value in subs.items():
        print(f'{sub_key} => {sub_value}')


get_score(Math=90, Science=80, Language=70)
print('-'*60)
get_score(Logic=70, Problems=60)

print('-'*60)


def get_people_scores(name, **skills):
    if len(skills) > 1:
        print(f'Hello {name} This Is Your Score Table:')
        for key, value in skills.items():
            print(f'{key} => {value}')
    else:
        print(f'Hello {name} You Have No Scores To Show')


get_people_scores("Osama", Math=90, Science=80, Language=70)
print('-'*60)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print('-'*60)
get_people_scores("Ahmed")
print('-'*60)
scores_list = {
    'Math': 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(name='nothing', **scores):
    if len(scores) > 1:
        if name != 'nothing':
            print(f'Hello {name} This Is Your Score Table Of Scores:')
        for key, value in scores.items():
            print(f'{key} => {value}')
    else:
        print(f'Hello {name} You Have No Scores To Show')


get_the_scores("Osama", **scores_list)
print('-'*60)
get_the_scores("Osama")
print('-'*60)
get_the_scores(**scores_list)  # type: ignore

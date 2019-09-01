import random

#shoutout to GeeksforGeeks for the list assist!
list_nouns = list(input("Enter at least two plural nouns: ").split())
while (len(list_nouns) < 2):
    list_nouns = list(input("Enter at least two plural nouns again: ").split())

list_jobs = list(input("Enter at least three jobs: ").split())
while len(list_jobs) < 3:
    list_jobs = list(input("Enter at least three jobs again: ").split())

list_animals =  list(input("Enter at least three animals: ").split())
while len(list_animals) < 3:
    list_animals =  list(input("Enter at least three animals again: ").split())

list_place = list(input("Enter at least two places: ").split())
while len(list_place) < 2:
    list_place = list(input("Enter at least two places again: ").split())

list_verb = list(input("Enter at least three verbs: ").split()) 
while len(list_verb) < 3:
    list_verb = list(input("Enter at least three verbs again: ").split())

lst_noun = list(input("Enter at least two nouns: ").split())
while len(lst_noun) < 2:
    lst_noun = list(input("Enter at least two nouns again: ").split())

plural_noun = str(random.choice(list_nouns))
occupation = str(random.choice(list_jobs))
animal = str(random.choice(list_animals))
place = str(random.choice(list_place))
verb = str(random.choice(list_verb))
noun = str(random.choice(lst_noun))


#prompt =

print(plural_noun)

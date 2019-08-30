#shoutout to GeeksforGeeks for the list assist!
list_nouns = list(input("Enter at least two plural nouns: ").split())
while len(list_nouns) == 0:
    list_nouns = list(input("Enter at least two plural nouns again: ").split())

list_jobs = list(input("Enter at least three jobs: ").split())
while len(list_jobs) == 0:
    list_jobs = list(input("Enter at least three jobs again: ").split())

list_animals =  list(input("Enter at least three animals: ").split())
while len(list_animals) == 0:
    list_animals =  list(input("Enter at least three animals again: ").split())
print(list_nouns)
print(list_jobs)
print(list_animals)
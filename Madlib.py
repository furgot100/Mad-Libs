#shoutout to GeeksforGeeks for the list assist!
list_noun = list(input("Enter at least two plural nouns: ").split())
while len(list_noun) == 0:
    list_noun = list(input("Enter at least two plural nouns again: ").split())
list_jobs = list(input("Enter at least three jobs: ").split())
while len(list_jobs) == 0:
    list_jobs = list(input("Enter at least three jobs again: ").split())
print(list_jobs)
print(list_noun)
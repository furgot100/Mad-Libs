#shoutout to GeeksforGeeks for the list assist!
list_noun = list(input("Enter at least two plural nouns: ").split())
while len(list_noun) == 0:
    list_noun = list(input("Enter at least two plural nouns again: ").split())

print(list_noun)
#fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.extend(new_friend)

#print the sorted list of our friends (without modifying the list itself)
print(sorted(friends))

#sort the list of friends alphabetically
friends.sort()

print(friends)

#print the list of friends as formatted text
print(', '.join(friends))
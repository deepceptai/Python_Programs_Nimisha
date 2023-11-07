
lucky_numbers = [4, 14, 24, 34, 42]
friends = ["Tom", "Carry", "Jim", "Kevin", "Tobby"]
#functions
friends2 = friends.copy()

friends.append("Oscar")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Oscar")
print(friends)

friends.reverse()
print(friends)

print(friends.index("Tom"))

friends.sort()
print(friends)

print(friends.pop())

friends.extend(lucky_numbers)
print(friends)

friends.clear()
print(friends)

print(friends2)

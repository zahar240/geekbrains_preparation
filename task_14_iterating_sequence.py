friend_name = "Aaaa"
friends = ["Aaaa", "Wwww", "Xxxx", "Qqqq", "Cccc"]
roles = ("admin", "quest", "user")

# Итерация через while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# Итерация через for
for i in friends:
    print(i)
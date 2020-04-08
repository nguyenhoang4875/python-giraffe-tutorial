lucky_numbers = [ 45,8,15,16,23,42]
friends = ["Kevin", "Karen","Jim", "Jim","Oscar","Toby"]

friends.insert(1,"Teo")

friends.append("Creed")

friends.extend(lucky_numbers)

friends.pop()

print(friends)

print(friends.count("Jim"))

friends2 = friends.copy();

print(friends2)

friends.clear()

lucky_numbers.sort()

lucky_numbers.reverse()

print(lucky_numbers)

first = "EL"
second = "E"
letters1 = ["Q", "W",  "E", "Y", "U", "D", "F", "J",  "Z", "X", "C", "V", "B"]
letters2 = ["Q", "W",   "Y", "U", "D", "F", "J",  "Z", "X", "C", "V", "B"]

for sub1 in letters1:
	for sub2 in letters2:
		print(sub1 + first + sub2 + second)

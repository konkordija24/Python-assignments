#this file can be used in music database of deephouse songs, and also has some functions



songSpecs = {"songName": "in my soul", "artist": "lovebirds", "genre": "deep house", "year": 2012, "durationMinutes": 4.67, "type": "love song", "tempo": "medium uptempo"}

for x in songSpecs:
    print x, ": ", songSpecs[x]


 def guessSpec(k,v):
 	k = input("Give your try on a key please: ")
 	v = input("Give your try on a value please: ")
for x in songSpecs:
	if x == k:
		for b in songSpecs:
			if songSpecs[b] == songSpecs[v]:
				return True
				print("Congratulations! You guessed right!")
			else:
				return False
				print("You lost! Try once again.")
	else:
		return False
		print ("You lost! Try once again.")			 

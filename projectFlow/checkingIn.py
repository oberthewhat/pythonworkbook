parrot = 'norwegian blue'

letter = input("enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))

else:
    print("I dont need that letter")
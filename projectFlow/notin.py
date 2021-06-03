activity = input("what would you like to do today: ")

if "cinema" not in activity.casefold():
    print("but i want to go to the cinema")


    # casefod() converts the input into a caseless match. does not convert to lowercase like in JS
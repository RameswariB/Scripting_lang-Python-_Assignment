locations = {0: "You are sleeping",
             1: "You are walking on a road",
             2: "You are at the top of a hill",
             3: "You are inside a building",
             4: "You are in a valley",
             5: "You are in the forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 4
while True:
    availableExits = ", ".join(exits[loc].keys())   
    print(locations[loc])
    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

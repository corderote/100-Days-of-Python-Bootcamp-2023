# ----------------------------------------------------------------------------- #
# Project Treasure Island.

print("Welcome to Treasure Island.\n\n\n")

print("You woke up in a deserted island, remembering nothing on how you got " 
      "there...\nYou got drunk?\n...\nOh yes, really drunk last night...\n"
      "Now you just remember the echoes of some pirates bragging about a huge"
      "treasure hidden somewhere inside a cavern inside a nowhere to find "
      "island.\nCould it be?\n...\nHow did I get here?\n...\n" "What should " 
      "I do?\nOnce your head slows down, you look up and admire the horizon,"
      "'where should I go next?'\nYou only see two options, go walking down "
      "the BEACH or go into the FOREST.\n"
      "Tip: TYPE 'BEACH' OR 'FOREST' TO CONTINUE:")

beach_or_forest = input("What will it be? \n")
beach_or_forest = beach_or_forest.lower()

if beach_or_forest == "beach":
    # Do beach stuff.
    print("Beach Stuff > __________")
    trace_or_raft = input("What will it be? \n")
    trace_or_raft = trace_or_raft.lower()
    if trace_or_raft == "trace":
        print("Trace Stuff > Found other pirates, party and get drunk again "
              "> Wrong END")
    elif trace_or_raft == "raft":
        print("Raft Stuff > __________")
    else: 
        print("GAME OVER")
elif beach_or_forest == "forest":
    # Do forest stuff
    print("Forest Stuff > __________")
    cave_or_deeper = input("What will it be? \n")
    cave_or_deeper = cave_or_deeper.lower()
    if cave_or_deeper == "cave":
        print("Cave Stuff > __________ \nSelect DOOR [1, 2 OR 3]: ")
        which_door = int(input("What will it be? \n"))
        if which_door == 1:
            print("BAD > Wrong END")
        elif which_door == 2:
            print("BAD > Wrong END")
        elif which_door == 3:
            print("You found the treasure. > Good END")
        else:
            print("Die of boredom > Wrong END")
    elif cave_or_deeper == "deeper":
        print("Deeper Stuff > Wrong END")
    else: 
        print("Deeper Stuff comes to you > Wrong END")
else:
    print("You tried to stand up but the headache is too much for you to even "
          "stand, you faint before you can even remember how you got there.\n "
          "You are still to drunk to even make a decision, your body will " 
          "lay there as a signal to other adventurers that come back to the " 
          " island looking for the treasure.\nYour corpse will be nothing but "
          "  another one that this island devours.\n\nGAME OVER\n")
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# Class Inheritance
# Allows us to take a class that we already have developed.
# We accomplish this by adding a pair of braces to our class creation
# and adding the name of the class we want to inherit from.
# In order to get hold of everything that our parent class has and is,
# all we have to do is to call "super().__init__()" where the super refers
# to the "super" class, which is the parent class that we associate.
class Animal:
    def __init__(self):
        self.name = "animal"

    def breath(self):
        print(f"{self.name}: I'm breathing")


class Fish(Animal):
    def __init__(self, name="Fish"):
        super().__init__()
        self.name = name

    def breath(self):
        super().breath()
        print("Doing it under water.")

    def swim(self):
        print(f"{self.name}: I'm swimming.")


nemo = Fish("Nemo")
nemo.swim()
nemo.breath()

# -----------------------------------------------------------------------------
# List Slicing:
# In python we have the ability to slice lists, dictionaries or tuples using
# their index values.
# For this we introduce the name of our item to slice, and then we set the values
# of the indexes that we want to set the bounds for our slice inside a pair of
# brackets, separating them with a colon.
# The slice does not include the last item that we set.

piano_keys_list = ["A", "B", "C", "D", "E", "F", "G"]
inner_list = piano_keys_list[2:5]
print(inner_list)
# This will print ['C', 'D', 'E']

# Not including the second parameter will make the list slice from the first
# parameter until the end.
inner_list = piano_keys_list[2:]
print(inner_list)
# This will print ['C', 'D', 'E', 'F', 'G']

# This works on the opposite direction as well
inner_list = piano_keys_list[:2]
print(inner_list)
# This will print ['A', 'B']

# If a third parameter is set, we are setting the step jump that we are going
# to make inside our list.

inner_list = piano_keys_list[1:5:2]
print(inner_list)
# This will print ['B', 'D']

# If we just specify the third parameter it will also work.
inner_list = piano_keys_list[::-1]
print(inner_list)
# This will print ['G', 'F', 'E', 'D', 'C', 'B', 'A']

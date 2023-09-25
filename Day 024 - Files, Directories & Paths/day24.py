# -----------------------------------------------------------------------------
# Files
file = open("my_file.txt")
file_content = file.read()
print(file_content)
file.close()

# The 'with' ... 'as' ... statement lets us open a file without having to worry
# about closing it. It works as an inner scope, and it will close the file once
# we exit such scope.
with open("my_file.txt") as file:
    file_content = file.read()
    print(file_content)


with open("my_file.txt", mode="a") as file:
    file.write("\nText to insert inside the file.")

# File opening modes:
# "r" > Read Only: Default mode, just allows us to read the document content.
# "w" > Write Only, destroys the content from the original document.
#       If the specified file does not exist it crates it.
# "a" > Append: Allows us to add content to the document without destroying
#       the content that was there previously.

# -----------------------------------------------------------------------------
# Paths
# Paths allow us to reach files that are not inside our project folder or that
# are inside other folders inside the project folder.
# We separate the folders using the forward slash sign '/'
# ABSOLUTE file paths start on the root of our system
# (macinctosh HD in MAC and the C: drive in Windows)
# Example: C:/Users/username/Desktop/my_file.txt
# Example: /Users/username/Desktop/my_file.txt
# RELATIVE file path works from the location of the file that is calling the
# other file, this location in known as working directory.
# The working directory sign is './' as current folder. If we want to go to the
# previous directory we use the '../' nomenclature to move up in the folder
# structure.
# '/' > Root ABSOLUTE file paths.
# './' > current working directory RELATIVE file path.
# '../' > parent folder of the working directory RELATIVE file path.

# Exercise > Move 'my_file.txt' to the desktop and use the ABSOLUTE path to
# get access to the file. And what if we wanted to use a RELATIVE path from
# the working directory?

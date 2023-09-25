# Find the names and save them as items inside a list.
mail_names = []
with open("./Input/Users/users.txt") as names_file:
    names = names_file.read()
    mail_names = names.split('\n')
    # names.readlines() does the same as names.split('/n') here but be
    # careful, as it wil keep the '\n' character for each line.
    # names.readlines() needs to also use the strip() function.

# Get the content of the letter that we want to send to everyone.
letter_file = open("./Input/Drafts/starting_letter.txt")
letter_content = letter_file.read()
letter_file.close()

# Create a new file for each name and change the general values for
# the users ones.
for name in mail_names:
    new_output_file_path = "./Output/letter_for_" + name + ".txt"
    new_output = open(new_output_file_path, "w")
    output_content = letter_content.replace("[name]", name)
    new_output.write(output_content)

# -----------------------------------------------------------------------------
import pandas

squirrel_data = pandas.read_csv("squirrel_data_central_park_2018.csv")
# Get the unique Fur Colours that the squirrels have as a list.
fur_colours = (squirrel_data["Primary Fur Color"].unique()[1:])
# Create a counter for each colour.
squirrel_counter = []
for color in fur_colours:
    squirrel_counter.append(0)
# Count the fur colours from our DataFrame
for squirrel_color in squirrel_data["Primary Fur Color"]:
    for index in range(len(fur_colours)):
        if squirrel_color == fur_colours[index]:
            squirrel_counter[index] += 1
# This also works to count every value:
# grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color" == "Gray"]])
# cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color" == "Cinnamon"]])
# grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color" == "Black"]])

# Create our dict
squirrel_count_dict = {
    "Fur Colour": fur_colours,
    "Count": squirrel_counter,
}
# Create and export our own DataFrame.
squirrel_count_df = pandas.DataFrame(squirrel_count_dict)
squirrel_count_df.to_csv("squirrel_count.csv")
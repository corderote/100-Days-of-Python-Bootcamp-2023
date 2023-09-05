# ----------------------------------------------------------------------------- #
# Loops.
# Loops are things that are ment to happen over and over again. 
# They allow us to execute the same block of code multiple times.

# For loop: 
list_of_items = [1, 2, 3]

for item in list_of_items:
    # Do things. 
    # Take care of the indentation of the code that you are going to write.
    # All the indented code is part of the loop that we are repeating.
    print(item)
    print("Item number: " + str(item))

print("Loop Ends.")

# range():
# As we are not going to use always the for loop with lists, when we want to 
# use the loop independently we use it in conjunction with the range() function.
# 'range()' generates an array of numbers, allowing us to loop between them.
# The range function can take up to 3 parameters, start, stop and step.
# The start parameter is 0 by default and will always be included.
# The stop parameter is never reached, our loop will stop at stop minus one.
# The step parameter sets the jumps value that we are going to take from the 
# start until we reach or surpass the stop argument. Its value is 1 by default.

total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)

# ----------------------------------------------------------------------------- #
# Exercise 1 - Average Height
# You are going to write a program that calculates the average student height 
# from a list of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
number_of_students = 0

for n in range(0, len(student_heights)):
    total_height += student_heights[n]
    number_of_students += 1
# Another option could be using the sum() function.
# This function allows us to sum the values from all the items in our list.
# But as we want to practise loops, we are going to avoid that option.

# You can also ignore the num of students and use the len(student_height).
average_height = round(total_height/number_of_students)
print(average_height)

# ----------------------------------------------------------------------------- #
# Exercise 2 - High Score
# You are going to write a program that calculates the highest score 
# from a list of scores.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
# Another option could be using the max() function.
# This function allows us to find the largest or highest item from a list.
# But as we want to practise loops, we are going to avoid that option.
print("The highest score in the class is: " + str(highest_score))
# print(f"The highest score in the class is: {highest_score}") also works.

# ----------------------------------------------------------------------------- #
# Exercise 3 - Adding Even Numbers
# You are going to write a program that calculates the sum of all the even 
# numbers from 1 to n. Where n is introduced by the user.

# 🚨 Don't change the code below 👇
input_number = int(input("Input a positive number: "))
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_numbers = 0
for number in range(0, input_number):
    if number % 2 == 0:
        sum_of_numbers += number
print(f"The sum of even numbers from 0 to {input_number} is equal to:") 
print(f"{sum_of_numbers}")

# ----------------------------------------------------------------------------- #
# Exercise 4 - FizzBuzz
# The program should automatically print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# If number is divisible by 3, instead of printing the number, print "Fizz".
# If number is divisible by 5, instead of printing the number, print "Buzz".
# And if the number is divisible by both, e.g. 15, print "FizzBuzz"

# 🚨 Don't change the code below 👇
input_number = int(input("Input a positive number: "))
# 🚨 Don't change the code above 👆
for number in range(1, input_number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# ----------------------------------------------------------------------------- #

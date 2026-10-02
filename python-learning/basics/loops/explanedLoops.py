#There are two types of loops in python
# 1 for Loop

# Iterating over a sequence of numbers using range()
# range(1,10) generates numbers from 1 to 9. Here range(staring point, ending point - 1, step size)
for i in range(1,10,4):
    print(i)

#A for loop is used to iterate over a sequence (like a list, tuple, string, or dictionary) or a range of numbers. It runs a predetermined number of times based on the size of the sequence.

list1 = ["apple", 2, 3, 4, 5]
for item in list1:
    print(item)

#2. The while Loop
#A while loop executes a block of code as long as a given condition remains true. You use it when you do not know in advance how many times the loop will need to run.

count = 1
while count <= 3:
    print(count)
    count += 1  # Crucial to update the condition, otherwise it creates an infinite loop


'''
Loop Control Statements
You can alter the behavior of both for and while loops using three key statements:
• break: Immediately terminates the loop entirely.
• continue: Skips the rest of the current iteration and jumps directly to the next one.
• pass: A null statement used as a placeholder when syntactic code is required, but you want no action taken.
'''
for num in range(1, 6):
    if num == 2:
        continue  # Skips printing 2
    if num == 4:
        break     # Stops the loop completely when reaching 4
    print(num)    # Output will only be 1 and 3
else:
    print("Loop finished successfully!") # This will only execute if the loop wasn't terminated by a break statement

# Nested Loops
# You can put a loop inside another loop. The inner loop runs completely for every single iteration of the outer loop.
for i in range(2):        # Outer loop
    for j in range(2):    # Inner loop
        print(f"i={i}, j={j}")

tree_rows = int(input("Enter tree height: ")) # Tree height input
start_space = tree_rows - 1 # Start position of the first hash
hashes = 1 # Initial number

# Save stumps spaces till later
first_spaces = start_space

# Make sure the right number of rows are printed
while start_space > 0:

# Print the spaces
    for i in range(start_space):
         print(" ", end="")

# Print the hashes
    for i in range(hashes):
        print("#", end="")

# Newline after each row is printed
    print()

# The spaces are decremented by 1 each
    start_space -= 1

# The hashes are incremented by 2
    hashes += 2

# Stump of the tree
for i in range(first_spaces):
    print(" ", end="")
print("#")




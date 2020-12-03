woods = []
with open("src/day3/day3_input.txt","r") as file:
    woods =  file.read().splitlines() 


print(len(woods))

start = True
index = 0
tree_counter = 0
#for line in range(len(woods) + 1):
for line in woods:
    if start:
        start = False
        continue

    index = index + 3

    if index >= len(line):
        index = index - len(line)
    
    s = line[:index] +"O" + line[index + 1:]
    print(s)

    if line[index] == "#":
        tree_counter = tree_counter + 1

print(tree_counter)

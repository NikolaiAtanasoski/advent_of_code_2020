
def puzzle_1():
    print(len(woods))

    start = True
    index = 0
    tree_counter = 0
    #   for line in range(len(woods) + 1):
    for line in woods:
        hitbox = "O"
        if start:
            print(line)
            start = False
            continue

        index = index + 3

        if index >= len(line):
            index = index - len(line)
    

        if line[index] == "#":
            hitbox = "X"
            tree_counter = tree_counter + 1

        s = line[:index] + hitbox + line[index + 1:]
        print(s)

    print(tree_counter)

def puzzle_2(steps_right, steps_down):
    start = True
    index = 0
    tree_counter = 0
    
    for line in range(0,len(woods),steps_down):
        hitbox = "0"
    
        if start:
            print(woods[line])
            start = False
            continue

        index = index + steps_right

        if index >= len(woods[line]):
            index = index - len(woods[line])

        if woods[line][index] == "#":
            hitbox = "X"
            tree_counter = tree_counter + 1

        s = woods[line][:index] + hitbox + woods[line][index + 1:]
        print(s)

    print(tree_counter)
    return tree_counter


woods = []
with open("src/day3/day3_input.txt","r") as file:
    woods =  file.read().splitlines() 

total = puzzle_2(1,1) * puzzle_2(3,1) * puzzle_2(5,1) * puzzle_2(7,1) * puzzle_2(1,2)

print(f"total: {total}")

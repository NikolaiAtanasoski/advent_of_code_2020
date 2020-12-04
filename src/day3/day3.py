import os


class Day3:

    def __init__(self):
        self.woods = self.load_input("day3_input.txt")

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            input_file = file.read().splitlines()
        return input_file

    def count_trees(self,steps_right, steps_down):
        position = -steps_right
        tree_counter = 0
        line_length = len(self.woods[0])
    
        for line in self.woods[::steps_down]:
            position = (position + steps_right) % line_length
            if line[position] == "#":
                tree_counter = tree_counter + 1

        print(tree_counter)
        return tree_counter

    def count_multiple(self,steps):
        answer = 1
        for step in steps:
            answer = answer * self.count_trees(step[0],step[1])
        return answer

    def print_tree_line(self, tree_line, position, hitbox):
        s = tree_line[:indpositionex] + hitbox + tree_line[position + 1:]
        print(s)

###main###


day3 = Day3()

puzzle_1_answer = day3.count_trees(3, 1)
print(f"puzzle_1_answer: {puzzle_1_answer}")

steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
puzzle_2_answer = day3.count_multiple(steps)
print(f"puzzle_2_answer: {puzzle_2_answer}")

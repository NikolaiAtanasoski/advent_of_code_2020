import os

class Day9:

    def __init__(self):
        self.input_data = self.load_input("day9_input.txt")

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()

    def format_input(self):
        data = []
        
        for line in self.input_data:
            data.append(line)

        return data

    def puzzle1(self):
        data = self.format_input()



        return data

    def puzzle2(self):
        data = self.format_input()



        return data


day9 = Day9()

answer1 = day9.puzzle1()
print(f"Answer 1 : {answer1}")

answer2 = day9.puzzle2()
print(f"Answer 2 : {answer2}")
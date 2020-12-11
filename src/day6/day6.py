import os

class Day6:

    input_data = None

    def __init__(self):
        self.input_data = self.load_input("day6_input.txt")

    def load_input(self,file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        data = []
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()
         

    def puzzle1(self):
        data = []
        _set = set()
        for line in self.input_data:
            if(line == ""):
                data.append(_set)
                _set = set()
            else:
                _set.update([answer for answer in line])
        
        data.append(_set)
        
        sum_of_answers = 0
        for set_of_answers in data:
            sum_of_answers = sum_of_answers + len(set_of_answers)
        
        return sum_of_answers

    def puzzle2(self):
        data = []
        _list = []
        for line in self.input_data:
            if(line == ""):
                data.append(_list)
                _list = []
            else:
                _list.append(set(line))

        data.append(_list) 

        sum_of_answers = 0
        for list_of_answer_sets in data:
            sum_of_answers = sum_of_answers + len(set.intersection(*list_of_answer_sets))
        
        return sum_of_answers



day6 = Day6()
answer1 = day6.puzzle1()
print(f"Answer 1: {answer1}")

answer2 = day6.puzzle2()
print(f"Answer 2: {answer2}")
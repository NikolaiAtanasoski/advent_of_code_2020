import os
import copy
class Day8:

    def __init__(self):
        self.input_data = self.load_input("day8_input.txt")

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()

    def format_input(self):
        data = []
        for line in self.input_data:
            instruction = [line.split(" ")[0],line.split(" ")[1]]
            data.append(instruction)
        return data

    def puzzle1(self):
        instructions = self.format_input()

        accumulator = 0
        already_run = set()
        i = 0 

        while i < len(instructions):
            if i in already_run:
                return accumulator
            else:
                already_run.add(i)
                operation = instructions[i][0]
                argument = instructions[i][1]
                if operation == "acc":
                    accumulator += int(argument)
                    i += 1
                elif operation == "jmp":
                    i += int(argument) 
                else:
                    i += 1

        return instructions

    def puzzle2(self):
        instructions = self.format_input()
        indices_jmp = [i for i, x in enumerate(instructions) if x[0] == "jmp"]
        indices_nop = [i for i, x in enumerate(instructions) if x[0] == "nop"]
        for i in indices_jmp:
            print(instructions)
            list_to_try = copy.deepcopy(instructions)
            list_to_try[i][0] = "nop"
            result = self.try_instructions(list_to_try)
            if result[0] == True:
                print(instructions)
                print(f"AMK JMP TO NOP AT INDEX {i}")
                return result[1]
        
        for i in indices_nop:
            list_to_try = copy.deepcopy(instructions)
            list_to_try[i][0] = "jmp"
            result = self.try_instructions(list_to_try)
            if result[0] == True:
                print(f"AMK NOP TO JMP AT INDEX {i}")
                return result[1]
    
        return "NOOO"

    def try_instructions(self,instructions):
        
        accumulator = 0
        already_run = set()
        i = 0 

        while i < len(instructions):
            if i in already_run:
                return (False,0)
            else:
                already_run.add(i)
                operation = instructions[i][0]
                argument = instructions[i][1]
                if operation == "acc":
                    accumulator += int(argument)
                    i += 1
                elif operation == "jmp":
                    i += int(argument) 
                else:
                    i += 1

        return (True,accumulator)



Day8 = Day8()

answer1 = Day8.puzzle1()
print(f"Answer 1 : {answer1}")

answer2 = Day8.puzzle2()
print(f"Answer 2 : {answer2}")
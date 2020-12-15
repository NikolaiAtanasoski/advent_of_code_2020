import os


class Day10:

    def __init__(self):
        self.input_data = self.load_input("day10_input.txt")

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()

    def format_input(self):
        data = []

        for line in self.input_data:
            data.append(int(line))

        return data

    def puzzle1(self):
        jolt_adapters = self.format_input()

        current_jolt = 0
        joltage_differences = {1:0,2:0,3:1} # 3 has 1 extra for laptop jolt
        laptop_jolt = max(jolt_adapters)
        while current_jolt != laptop_jolt:
            for i in range(1,4):
                tried_jolt = self.find_jolt(jolt_adapters,current_jolt,i)
                if tried_jolt != None:
                    current_jolt = tried_jolt
                    joltage_differences[i] += 1
                    break
            

        print(joltage_differences)
        return joltage_differences[1] * joltage_differences[3]

    def find_jolt(self,jolt_adapters,current_value, jolt_value):
        for adapter in jolt_adapters:
            if current_value + jolt_value == adapter:
                return adapter
        return None

    def puzzle2(self):
        data = self.format_input()

        return data


day10 = Day10()

answer1 = day10.puzzle1()
print(f"Answer 1 : {answer1}")

# answer2 = day10.puzzle2(133015568)
# print(f"Answer 2 : {answer2}")

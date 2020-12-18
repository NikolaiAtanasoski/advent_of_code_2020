import os


class Day10:

    def __init__(self):
        self.input_data = self.load_input("day10_input.txt")
        self.path_dict = dict()

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
        jolt_adapters = self.format_input()
        laptop_jolt = max(jolt_adapters)

        jolt_adapters.sort(reverse=True)

        for jolt_adapter in jolt_adapters:
            self.path_dict[jolt_adapter] = list()
            for next_jolt in self.possible_next_jolts(jolt_adapters,jolt_adapter):
                self.path_dict[jolt_adapter].append(next_jolt)

        print(jolt_adapters)
        print(self.path_dict)
        print(self.amk(48))
        return 0

    def amk(self, key):
        count = 0
        for v in self.path_dict[key]:
            count += self.amk(v)

        count += len(self.path_dict[key])
        return count 

    def tree_search(self,jolt_adapters,current_jolt, max_jolt):
        count = 0
        
        if(current_jolt == max_jolt):
            return 1
        
        for adapter in self.possible_next_jolts(jolt_adapters,current_jolt):
            print(f"current Jolt {adapter}")
            next_jolt_adapters = [x for x in jolt_adapters if x > adapter]
            count += self.tree_search(next_jolt_adapters,adapter, max_jolt)

        return count

    def possible_next_jolts(self,jolt_adapters,current_jolt):
        ret = list()
        for jolt_adapter in jolt_adapters:
            if jolt_adapter - current_jolt in (1,2,3):
                ret.append(jolt_adapter)
        
        print(f"Next possible adapters : {ret}")
        return ret

    


day10 = Day10()

answer1 = day10.puzzle1()
print(f"Answer 1 : {answer1}")

answer2 = day10.puzzle2()
print(f"Answer 2 : {answer2}")

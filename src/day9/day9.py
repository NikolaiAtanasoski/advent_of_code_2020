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
            data.append(int(line))

        return data

    def puzzle1(self, preamble_length):
        numbers = self.format_input()


        for i in range(preamble_length,len(numbers) - 1):
            print(f"next number: {numbers[i]}")
            possible_next_numbers = self.possible_results(numbers[i-preamble_length:i])
            if numbers[i] not in possible_next_numbers:
                return numbers[i]
            

        return None
    
    def possible_results(self, numbers):
        possible_results = list()
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                possible_results.append(numbers[i]+numbers[j])
          
        print(f"Numbers: {numbers} results: {possible_results}\n")
        return possible_results
    
    def puzzle2(self, number):
        numbers = self.format_input()

        for i in range(len(numbers)):
            result = numbers[i]
            result_set = {numbers[i]}
            for j in range(i+1,len(numbers)):
                result += numbers[j]
                result_set.add(numbers[j])
                if result == number:
                    return max(result_set) + min(result_set)
                elif result > number:
                    break

        return None



day9 = Day9()

# answer1 = day9.puzzle1(5)
# print(f"Answer 1 : {answer1}")

answer2 = day9.puzzle2(133015568)
print(f"Answer 2 : {answer2}")
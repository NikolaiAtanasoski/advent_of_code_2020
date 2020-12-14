import os


class Day7:

    def __init__(self):
        self.input_data = self.load_input("day7_input.txt")

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        data = []
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()

    def format_input(self):
        bags = {}

        # create the dictionary
        for rule in self.input_data:
            upper_bag = rule.split("s contain")[0].strip()

            inner_bags_rules = rule.split("s contain")[1].strip()[:-1]  # strip empty spaces and remove dot
            bags[upper_bag] = {}
            if "no other bags" not in inner_bags_rules:
                for inner_bag_rule in inner_bags_rules.split(","):
                    count = inner_bag_rule.strip().split(" ", 1)[0]
                    inner_bag = inner_bag_rule.strip().split(" ", 1)[1]
                    if inner_bag[-1] == "s":
                        inner_bag = inner_bag[:-1]
                    bags[upper_bag][inner_bag] = count

        return bags

    def puzzle1(self):

        bags = self.format_input()
        list_of_bags = self.recursive_find_bag(bags, "shiny gold bag")

        return len(set(list_of_bags))

    def recursive_find_bag(self, bags, bagname):
        list_of_bags = []
        for key, content in bags.items():
            if bagname in content.keys():
                list_of_bags.append(key)
                _bags = self.recursive_find_bag(bags, key)
                list_of_bags.extend(_bags)

        return list_of_bags

    def puzzle2(self):
        bags = self.format_input()
        print(bags)

        number_of_bags = self.recursive_count_bag(bags, "shiny gold bag", 0)

        print(number_of_bags)
        return number_of_bags

    def recursive_count_bag(self, bags, bagname,bag_count):
        sum_bag_count = 0

        for new_bagname,number_of_bags in bags[bagname].items():
            sum_bag_count += int(number_of_bags)
            sum_bag_count += int(number_of_bags) * self.recursive_count_bag(bags,new_bagname,number_of_bags)

        return sum_bag_count


day7 = Day7()

answer1 = day7.puzzle1()
for k,v in answer1.items():
    print(k,v)
print(f"Answer 1: {answer1}")

answer2 = day7.puzzle2()
print(f"Answer 2: {answer2}")

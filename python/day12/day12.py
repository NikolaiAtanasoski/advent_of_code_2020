import os


class Cardinal:
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

    COMPASS = [NORTH, EAST, SOUTH, WEST]


class Day12:

    def __init__(self):
        self.input_data = self.load_input("day12_input.txt")
        self.x = 0
        self.y = 0
        self.current_direction = Cardinal.EAST

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
        instructions = self.format_input()

        for instruction in instructions:

            action = instruction[0]
            value = instruction[1:]
            if action in Cardinal.COMPASS:
                self.move_in_direction(direction=action, value=int(value))

            else:
                if action in ["L", "R"]:
                    self.current_direction = self.rotate_by(
                        direction=action, degrees=int(value))
                else:
                    self.move_in_direction(
                        direction=self.current_direction, value=int(value))

        print(f"x={self.x} y={self.y}")
        return abs(self.x) + abs(self.y)

    def move_in_direction(self, direction, value=int):

        if direction == Cardinal.NORTH:
            self.y += value
        elif direction == Cardinal.SOUTH:
            self.y -= value
        elif direction == Cardinal.EAST:
            self.x += value
        else:
            self.x -= value

    def rotate_by(self, direction, degrees):

        if direction == "R":
            compass = Cardinal.COMPASS
        else:
            compass = Cardinal.COMPASS[::-1]

        new_direction = int(degrees / 90)
        new_direction = new_direction + compass.index(self.current_direction)
        new_direction = new_direction % 4
        return compass[new_direction]

    def puzzle2(self):
        instructions = self.format_input()

        waypoint = {"x": 10, "y": 1}
        ship = {"x": 0, "y": 0}
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            if action == "F":
                x = waypoint["x"] * value
                y = waypoint["y"] * value
                ship["x"] = ship["x"] + x
                ship["y"] = ship["y"] + y

            elif action == "N":
                waypoint["y"] = waypoint["y"] + value
            elif action == "E":
                waypoint["x"] = waypoint["x"] + value
            elif action == "S":
                waypoint["y"] = waypoint["y"] - value
            elif action == "W":
                waypoint["x"] = waypoint["x"] - value

            elif action == "R":
                print("rotate Right")
                for x in range(int(value/90)):
                    new_x = waypoint["y"]
                    waypoint["y"] = waypoint["x"] * -1
                    waypoint["x"] = new_x  
            elif action == "L":
                print("rotate Left")
                for x in range(int(value/90)):
                    new_y = waypoint["x"]
                    waypoint["x"] = waypoint["y"] * -1  
                    waypoint["y"] = new_y
                    

            print(f"waypoint x={waypoint['x']} y={waypoint['y']}")
            print(f"ship x={ship['x']} y={ship['y']}\n")

        return abs(ship["x"]) + abs(ship["y"])


day12 = Day12()

answer1 = day12.puzzle1()
print(f"Answer 1 : {answer1}")

answer2 = day12.puzzle2()
print(f"Answer 2 : {answer2}")

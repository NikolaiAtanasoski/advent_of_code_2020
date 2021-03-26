import os


class Cardinal:
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

    COMPASS = [NORTH, EAST, SOUTH, WEST]


class Day13:

    def __init__(self):
        self.input_data = self.load_input("day13_input.txt")
        self.x = 0
        self.y = 0
        self.current_direction = Cardinal.EAST

    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            return file.read().splitlines()

    def puzzle1(self):
        time = int(self.input_data[0]) 
        bus_ids = [int(_id) for _id in self.input_data[1].split(",") if _id != "x"] 

        print(time)
        print(bus_ids)

        dep_times = {}
        for bus_id in bus_ids:
            next_dep = (int(time / bus_id) + 1) * bus_id
            dep_times[bus_id] = next_dep

        bus_id = min(dep_times, key=dep_times.get)
        waiting_time = dep_times[bus_id] - time

        return waiting_time * bus_id

    def puzzle2(self):
        bus_ids = [_id for _id in self.input_data[1].split(",")]
        
        
        bus_dict = {}
        first_bus = int(bus_ids[0])
        largest_bus_id = 0
        largest_bus_offset = 0 
        for pos in range(1,len(bus_ids)):
            if bus_ids[pos] != "x":
                bus_id = int(bus_ids[pos])
                bus_dict[pos] = bus_id
                if largest_bus_id < bus_id:
                    largest_bus_id = bus_id
                    largest_bus_offset = pos

        
        print(largest_bus_id)
        print(largest_bus_offset)
        found = False
        time = 0
        while not found:
            # print(time)
            found = True
            for minutes, bus_id in bus_dict.items():
                if (time + minutes) % bus_id != 0:
                    found = False
                    break
            
            time = time + (len(bus_ids) - 1) + largest_bus_id - largest_bus_offset  + 1 
            # while time % first_bus != 0:
            #     time += largest_bus_id - largest_bus_offset

        # print(time - first_bus)
        return time - first_bus

day13 = Day13()

answer1 = day13.puzzle1()
print(f"Answer 1 : {answer1}")

answer2 = day13.puzzle2()
print(f"Answer 2 : {answer2}")

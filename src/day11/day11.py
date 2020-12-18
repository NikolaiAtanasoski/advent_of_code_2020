import os


class Seat:
    FLOOR = "."
    OCCUPIED = "#"
    EMPTY = "L"


class Day11:

    def __init__(self):
        self.input_data = self.load_input("day11_input.txt")

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
        seats = self.format_input()
        old_seats = list()
        new_seats = list(seats)
        counter = 0

        while new_seats != old_seats:
            old_seats = list(new_seats)
            new_seats = self.populate_seats(old_seats)
            
            print(f"Round: {counter}")
            self.print_seats(new_seats)
            counter += 1

        
        return self.count_seats(new_seats)

    def count_seats(self,seats):
        count = 0

        for row in seats:
            for seat in row:
                if seat == Seat.OCCUPIED:
                    count += 1

        return count

    def print_seats(self,seats):
        for row in seats:
            print(f"{row}")
        print("")

    def populate_seats(self, seats):
        new_seats = list()
        for row in range(len(seats)):
            new_row = ""
            for seat_number in range(len(seats[row])):
                if seats[row][seat_number] == Seat.EMPTY:
                    if self.are_adjacent_seats_empty(seats, row, seat_number):
                        new_row = new_row + Seat.OCCUPIED
                    else:
                        new_row = new_row + seats[row][seat_number]
                elif seats[row][seat_number] == Seat.OCCUPIED:
                    if self.are_four_or_more_adjacent_seats_occupied(seats, row, seat_number):
                        new_row = new_row + Seat.EMPTY
                    else:
                        new_row = new_row + seats[row][seat_number]
                else:
                    new_row = new_row + seats[row][seat_number]

            new_seats.append(new_row)



        return new_seats

    def are_four_or_more_adjacent_seats_occupied(self, seats, row, seat_number):
        seat_coordinate = (row, seat_number)
        count = 0

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if self.is_seat_occupied(seats, seat_coordinate, (i, j)):
                    count += 1

        return count >= 4

    def are_adjacent_seats_empty(self, seats, row, seat_number):
        seat_coordinate = (row, seat_number)

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if not self.is_seat_empty(seats, seat_coordinate, (i, j)):
                    return False

        return True

    def is_seat_occupied(self,seats, seat_coordinate, offset):
        return self.get_seat_kind(seats, seat_coordinate, offset) == Seat.OCCUPIED

    def is_seat_empty(self, seats, seat_coordinate, offset):
        return self.get_seat_kind(seats, seat_coordinate, offset) != Seat.OCCUPIED

    def get_seat_kind(self, seats, seat_coordinate, offset):
        if offset == (0, 0):
            return ""

        row = seat_coordinate[0] + offset[0]
        if row < 0 or row >= len(seats):
            return ""

        seat_number = seat_coordinate[1] + offset[1]
        if seat_number < 0 or seat_number >= len(seats[0]):
            return ""

        seat = seats[row][seat_number]
        return seat

    def puzzle2(self):
        data = self.format_input()

        return data


day11 = Day11()

answer1 = day11.puzzle1()
print(f"Answer 1 : {answer1}")

# answer2 = day11.puzzle2(133015568)
# print(f"Answer 2 : {answer2}")

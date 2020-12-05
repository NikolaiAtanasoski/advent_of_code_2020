import os

class Day5:

    def __init__(self):
        self.data = self.load_input("day5_input.txt")

    def load_input(self,file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            input_file = file.read().splitlines()
        
        # data = []
        # for line in input_file:
        #     if len(line) == 0:
        #         data.append("")
        #     else:
        #         for field in line.split():
        #             data.append(field)

        return input_file


    def puzzle(self):
        lower_row_half = "F"
        uppper_row_half = "B"

        lower_column_half = "L"
        uppper_column_half = "R"

        seat_id_list = []
        
        
        for seat_info in self.data:
            
            row = list(range(0,128))
            for row_info in seat_info[:7]:
                if row_info == lower_row_half:
                    row = row[:int(len(row)/2)]
                else:
                    row = row[int(len(row)/2):]

            if row == 0 or row == 127:
                continue

            column = list(range(0,8))
            for column_info in seat_info[7:]:
                if column_info == lower_column_half:
                    column = column[:int(len(column)/2)]
                else:
                    column = column[int(len(column)/2):]
            
            # seat_id = self.get_seat_id(row[0],column[0])
            seat_id_list.append(self.get_seat_id(row[0],column[0]))
            # if largest_number < seat_id:
            #     largest_number = seat_id
            
        seat_id_list.sort()
        last_number = seat_id_list[0]
        for i in range(0,len(seat_id_list) - 1):
            if seat_id_list[i] + 1 != seat_id_list[i+1]:
                return seat_id_list[i] + 1


    
        return missing_seat_id

    def get_seat_id(self,row,column):
        return row * 8 + column


##main###

day5 = Day5()

answer = day5.puzzle()
print(f"\nAnswer: {answer}")
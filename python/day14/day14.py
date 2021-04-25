import os


binary_zero = "00000000000000000000000000000000"

class MaskHelper:
    def __init__(self,bitmask):
        self.mask = bitmask
        self.mem_instructions = []

class MemInstruction:
    def __init__(self,address, value):
        self.address = address
        binary = format(int(value),"b")  
        self.value = binary.zfill(36)


class Day14:

    def __init__(self):
        self.input_data = self.load_input("day14_input.txt")
        # self.input_data = self.load_input("example_input.txt")
        
    def load_input(self, file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            line_list = file.read().splitlines() 
        
        data = []
        last_helper = None
        for line in line_list:
            if line.startswith("mask"):
                data.append(last_helper)
                mask = line.split(" ")[2]
                last_helper = MaskHelper(mask)
            if line.startswith("mem"):
                value = line.split(" ")[2]
                address_begin = line.index("[")
                address_end = line.index("]")
                address = line[address_begin + 1:address_end]
                memory_helper = MemInstruction(address,value)
                last_helper.mem_instructions.append(memory_helper)
        
        del data[0]
        data.append(last_helper)
        return data
        # return file.read().splitlines()

    def puzzle1(self):
        mem_dict = {}
        for mask_helper in self.input_data:
            mask = mask_helper.mask
            for instruction in mask_helper.mem_instructions:
                value, address = instruction.value, instruction.address
                if address not in mem_dict.keys():
                    mem_dict[address] = binary_zero 
                masked_binary_value = self.mask_binary_value(mask, value)
                new_value = int(masked_binary_value,2) # + int(mem_dict[address],2)
                mem_dict[address] = bin(new_value)[2:].zfill(36)

        result_sum = 0
        for key, value in mem_dict.items():
            print(key, value)
            result_sum += int(value,2)
        print("AMK")
        print(result_sum)
        return result_sum

    def mask_binary_value(self,mask, value) -> str:
        masked_value = str(value)
        for index, char in enumerate(mask):
            if char != "X":
                masked_value = masked_value[:index] + char +  masked_value[index+1:]
                
        return masked_value

    def puzzle2(self):
        mem_dict = {}
        for mask_helper in self.input_data:
            mask = mask_helper.mask
            for instruction in mask_helper.mem_instructions:
                value, address = instruction.value, instruction.address
                masked_address = self.apply_mask(mask, address)
                addresses = self.run_that_shit(masked_address,0)
                for address in addresses:
                    # print(int(address,2), address)
                    mem_dict[address] = value

        result_sum = 0
        for key, value in mem_dict.items():
            result_sum += int(value,2)
        
        return result_sum

    def apply_mask(self, mask, address) -> str:
        adresses = set()
        masked_address = bin(int(address))[2:].zfill(36)
        # print(f"address:        {masked_address}")
        # print(f"mask   :        {mask}")
        for index, char in enumerate(mask):
            if char != "0":
                masked_address = masked_address[:index] + char +  masked_address[index+1:]
        # print(f"masked address: {masked_address}")
        return masked_address

    def run_that_shit(self, masked_address, startindex:int) -> set:
        address_list = []
        if startindex > 35 or "X" not in masked_address:
            return [] 
        for index, char in enumerate(masked_address[startindex:],startindex):
            if char == "X":
                adr1 = masked_address[:index] + "1" +  masked_address[index+1:]
                address_list.extend(self.run_that_shit(adr1, index+1))
                adr2 = masked_address[:index] + "0" +  masked_address[index+1:]
                address_list.extend(self.run_that_shit(adr2, index+1))
                break
        
        if "X" not in adr1:
            address_list.append(adr1)
        if "X" not in adr2:
            address_list.append(adr2)

        return set(address_list)

        
day14 = Day14()

# answer1 = day14.puzzle1()
# print(f"Answer 1 : {answer1}")

answer2 = day14.puzzle2()
print(f"Answer 2 : {answer2}")

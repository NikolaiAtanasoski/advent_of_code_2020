import os

class Day4:

    FIELDS_NEEDED = ("byr","iyr","eyr","hgt","hcl","ecl","pid")
    FIELDS_OPTIONAL = ("cid",)

    def __init__(self):
        self.passport_data = self.load_input("day4_input.txt")

    def load_input(self,file_name):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, file_name), "r") as file:
            input_file = file.read().splitlines()
        
        data = []
        for line in input_file:
            if len(line) == 0:
                data.append("")
            else:
                for field in line.split():
                    data.append(field)

        return data

    def split_to_dict(self):
        data_dict = []
        _data = {}
        for data in self.passport_data:
            if len(data) == 0 :
                data_dict.append(_data)
                _data = {}
            else:
                key=data.split(":")[0]
                value=data.split(":")[1]
                _data[key] = value

        data_dict.append(_data)
        return data_dict

    def puzzle1(self):
        passports_data = self.split_to_dict()
        valid_passports = 0

        for data in passports_data:
            if set(self.FIELDS_NEEDED).issubset(set(data.keys())):
                valid_passports = valid_passports + 1
            else:
                print(data.keys())
                print(f"self_keys({self.FIELDS_NEEDED})")

        
        
        return valid_passports

    
    def is_valid(self,data):
        byr = data.get("byr")
        _byr = int(data.get("byr"))
        if len(byr) != 4 or 1920 > _byr or _byr > 2002:
            print(byr)
            return False
        
        iyr = data.get("iyr")
        _iyr = int(data.get("iyr"))
        if len(iyr) != 4 or 2010 > _iyr or _iyr > 2020:
            print(iyr)
            return False
        
        eyr = data.get("eyr")
        _eyr = int(data.get("eyr"))
        if len(eyr) != 4 or 2020 > _eyr or _eyr > 2030:
            print(eyr)
            return False

        hgt = data.get("hgt")
        if len(hgt) < 3:
            return False
        _height = int(hgt[:-2])
        if hgt[-2:] == "cm" and (_height < 150 or _height > 193):
            print(hgt)
            return False
        elif hgt[-2:] == "in" and (_height < 59 or _height >76):
            print(hgt)
            return False

        hcl = data.get("hcl")
        if hcl[0] != "#" or len(hcl) != 7 or not hcl[1:].isalnum():
            print(hcl)
            return False

        ecl = data.get("ecl")
        valid_ecl = ("amb","blu","brn","gry","grn","hzl","oth")
        if ecl not in valid_ecl:
            print(ecl)
            return False

        pid = data.get("pid")
        if len(pid) != 9 or not pid.isnumeric():
            print(pid)
            return False

        return True
    

    def puzzle2(self):
        passports_data = self.split_to_dict()
        valid_passports = 0

        for data in passports_data:
            if set(self.FIELDS_NEEDED).issubset(set(data.keys())) and self.is_valid(data):
                valid_passports = valid_passports + 1

        
        
        return valid_passports


## valid on byr, iyr, eyr, hgt, hcl, ecl , pid , optional(cid)
## fail on something missing except cid 

### main ###

day4 = Day4()

print(f"Answer: {day4.puzzle2()}")

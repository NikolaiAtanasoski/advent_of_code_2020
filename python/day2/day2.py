def get_input():
    passwords_with_policy = []
    with open("day2_input.txt","r") as file:
        for line in file:
            arr = line.split(" ")
            passwords_with_policy.append((arr[0],arr[1],arr[2]))
    return passwords_with_policy




def puzzle1_valid_on_char_count(input_list):
    valid_pw = 0

    for password_with_policy in input_list:
        min = int(password_with_policy[0].split("-")[0]) # tuble[0] is min max, substr at 0 -> (min)-max
        max = int(password_with_policy[0].split("-")[1]) # tuble[0] is min max, substr at 2 -> min-(max)
        char = password_with_policy[1][0]
        password = password_with_policy[2]
        count = password.count(char)
    
        if min <= count and count <= max:
            valid_pw = valid_pw + 1
            # print(f"min: {min} max: {max} char: {char} password: {password} charcount: {count}")
    
    print("Puzzle 1 Valid min-max char count:")
    print(f"valid pw total: {valid_pw} ")

def puzzle2_valid_on_char_position(input_list):
    valid_pw = 0
    for password_with_policy in input_list:
        pos1 = int(password_with_policy[0].split("-")[0]) # tuble[0] is min max, substr at 0 -> (pos1)-pos2
        pos2 = int(password_with_policy[0].split("-")[1]) # tuble[0] is min max, substr at 2 -> pos1-(pos2)
        char = password_with_policy[1][0]
        password = password_with_policy[2]
        # print(f"pos1: {pos1} pos2: {pos2} char: {char} password: {password} ")
        
        chars_in_position = 0
        #index information not beginning with 0 
        if char == password[pos1 - 1]:
            chars_in_position = chars_in_position + 1
        if char == password[pos2 - 1]:
            chars_in_position = chars_in_position + 1
        # print(f"chars in positions: {chars_in_position} ")
        if chars_in_position == 1:
            valid_pw = valid_pw + 1

    print("Puzzle 2 Valid either pos1 or pos2 char count:")
    print(f"valid pw total: {valid_pw} ")

## MAIN ##
input_list = get_input()
# input_list = [("1-3","a:","abcde"), ("1-3","b:","cdefg"), ("2-9","c:","ccccccccc")]

puzzle1_valid_on_char_count(input_list)

puzzle2_valid_on_char_position(input_list)
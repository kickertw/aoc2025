from utils.file_util import FileUtil


def find_joltage(input: list[int], joltage_len = 2) -> int:
    max_val = max(input[:(joltage_len-1)*-1])
    max_val_index = input.index(max_val)

    max_val_str = str(max_val)
    max_val = max(input[max_val_index+1:])
    max_val_str += str(max_val)
    return int(max_val_str)

# 123456 - 3
# 1st search, exclude last 2
# 2nd search, exclude:
#   - everything before and including first found index
#   - exclude last 1
# 3rd search, exclude:
#  - everything before and including 2nd found index
def find_joltage_v2(input: list[int], joltage_len = 2) -> int:
    max_val = max(input[:-(joltage_len-1)])
    max_val_str = str(max_val)    
    max_val_index = input.index(max_val)
    joltage_len -= 1
    
    while joltage_len > 0:
        if joltage_len > 1:
            new_input = input[max_val_index+1:-(joltage_len-1)]
        else:
            new_input = input[max_val_index+1:]

        max_val = max(new_input)
        max_val_index = new_input.index(max_val) + max_val_index + 1
        max_val_str += str(max_val)
        joltage_len -= 1

    return int(max_val_str)


def main():
    data = FileUtil.read_file('./inputs/day3.input.txt')

    p1_ans = 0
    p2_ans = 0
    for line in data:
        int_list = [int(item) for item in list(line)]
        joltage = find_joltage(int_list) # should be able to use v2 here too
        #print(joltage)
        p1_ans += joltage

        joltage = find_joltage_v2(int_list, 12)
        #print(joltage)
        p2_ans += joltage

    print(f"p1 = {p1_ans}")
    print(f"p2 = {p2_ans}")

if __name__ == "__main__":
    main()
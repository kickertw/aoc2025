from utils.file_util import FileUtil


def get_max_len(numbers: list[str]) -> int:
    max_len = 0
    for val in numbers:
        if len(val) > max_len:
            max_len = len(val)

    return max_len


def create_num_list(inputs: list[str]) -> list[list[int]]:
    ret_val = []

    # first row
    split_str = inputs[0].split()
    for num in split_str:
        ret_val.append([int(num)])

    for input in inputs[1:]:
        ii = 0
        split_str = input.split()
        for num in split_str:
            ret_val[ii].append(int(num))
            ii += 1

    return ret_val


def get_cephalopod_num(inputs: list[str], pos: int) -> int:
    temp_num = ""
    for input in inputs:
        if len(input) > pos:
            rev = input[::-1]
            temp_num += rev[pos]

    return int(temp_num)


def create_cephalopod_num_list(inputs: list[str]) -> list[list[int]]:
    ret_val = []

    # first row
    ii = len(inputs[0]) - 1

    temp_list = []
    while ii >= 0:
        temp_num = ""
        for input in inputs:
            temp_num += input[ii] if input[ii] != " " else ""

        if temp_num == "":
            ret_val.append(temp_list)
            temp_list = []
        else:
            temp_list.append(int(temp_num))

        ii -= 1

    ret_val.append(temp_list)
    return ret_val


def create_op_list(inputs: list[str]) -> list[str]:
    ret_val = []

    for input in inputs:
        split_str = input.split()
        for num in split_str:
            ret_val.append(num)

    return ret_val


def calculate(numbers: list[int], op: str) -> int:
    eval_str = str(numbers[0])
    for num in numbers[1:]:
        eval_str += f"{op}{num}"

    ret_val = eval(eval_str)
    return ret_val


def main():
    inputs = FileUtil.read_file("inputs/day6.input.txt")

    numbers_list = create_num_list(inputs[:-1])
    numbers_list_p2 = create_cephalopod_num_list(inputs[:-1])
    ops = create_op_list(inputs[-1])

    ii = 0
    running_sum = 0
    for numbers in numbers_list:
        sum = calculate(numbers, ops[ii])
        ii += 1
        # print(f"sum = {sum}")
        running_sum += sum

    print(f"p1 = {running_sum}")
    print()

    ii = 0
    running_sum = 0
    ops.reverse()
    for numbers in numbers_list_p2:
        sum = calculate(numbers, ops[ii])
        ii += 1
        # print(f"sum = {sum}")
        running_sum += sum

    print(f"p2 = {running_sum}")


if __name__ == "__main__":
    main()

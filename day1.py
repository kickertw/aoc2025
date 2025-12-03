from utils.file_util import FileUtil

def turn_dial(current_location: int, direction: str, distance: int) -> int:
    '''
    Returns the new locations of where the dial is pointing
    '''
    if direction == 'L':
        distance = distance * -1

    current_location = current_location + distance

    while current_location > 99 or current_location < 0:
        if current_location > 99:
            current_location = current_location - 100
        elif current_location < 0:
            current_location = 100 + current_location

    return current_location

def turn_dial_v2(start_location: int, direction: str, distance: int) -> tuple[int, int]:
    '''
    Returns the new locations of where the dial is pointing
    '''
    og_instruction = f"{direction}{distance}"
    
    mod = distance % 100
    passed_zero = abs(distance) // 100
    mod_distance = distance - (passed_zero * 100)

    if direction == 'L':
        mod_distance = mod_distance * -1

    if mod == 0:
        return start_location, passed_zero

    new_location = start_location + mod_distance    
    if new_location > 99:
        new_location = new_location - 100
        passed_zero += 1
    elif new_location < 0:
        new_location = 100 + new_location
        if start_location != 0:
            passed_zero += 1
    elif new_location == 0 and start_location == abs(mod_distance):
        passed_zero += 1

    debug_output = f"The dial is rotated {og_instruction} to point at {new_location}; during this rotation, it points at 0 {passed_zero}-times (passed_zero = {passed_zero})"
    print(debug_output)
    return new_location, passed_zero

def main():
    data = FileUtil.read_file('./aoc25/inputs/day1.txt')

    current_location_p1 = 50
    zero_counter = 0

    current_location_p2 = 50
    zero_counter_p2 = 0

    print("The dial starts by pointing at 50.")
    for line in data:
        direction = line[0]
        distance = int(line[1:])

        current_location_p1 = turn_dial(current_location_p1, direction, distance)
        current_location_p2, zero_counter_temp = turn_dial_v2(current_location_p2, direction, distance)
        zero_counter_p2 += zero_counter_temp
        
        if current_location_p1 == 0:
            zero_counter += 1

        # if current_location_p2 == 0:
        #     zero_counter_p2 += 1  # For part 2, hitting zero exactly counts as well

    print (f"Part 1 Password = {zero_counter}")
    print (f"Part 2 Password = {zero_counter_p2}")

if __name__ == "__main__":
    main()
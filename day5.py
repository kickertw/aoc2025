import time
from utils.file_util import FileUtil

def create_valid_id_set(input: list[str]) -> set[tuple[int, int]]:
    ranges = set()

    for part in input:
        bounds = part.split('-')
        low = int(bounds[0])
        high = int(bounds[1])

        print(f"Adding range {low}-{high}")

        # Check if the low is already in a range in the set
        add_range = True
        for existing_range in ranges:
            if low < existing_range[0] and existing_range[1] < high:
                # The new range completely covers the existing range
                ranges.remove(existing_range)
                ranges.add((low, high))
                add_range = False
                break
            if existing_range[0] <= low <= existing_range[1] and high > existing_range[1]:
                # Extend the existing range
                ranges.remove(existing_range)
                ranges.add((existing_range[0], high))
                add_range = False
                break
            if existing_range[0] <= high <= existing_range[1] and low < existing_range[0]:
                # Extend the existing range
                ranges.remove(existing_range)
                ranges.add((low, existing_range[1]))
                add_range = False
                break
            if existing_range[0] <= low <= existing_range[1] and existing_range[0] <= high <= existing_range[1]:
                add_range = False
                break

        if add_range:
            ranges.add((low, high))

    return ranges

def create_valid_id_list(input: list[str]) -> list[tuple[int, int]]:
    """
    Creates a list of valid id ranges. Also merges overlapping ranges together
    """
    ranges = []

    for part in input:
        bounds = part.split('-')
        low = int(bounds[0])
        high = int(bounds[1])
        ranges.append((low, high))

    ranges.sort()

    # Check if the low is already in a range in the set
    temp_range = (ranges[0][0], ranges[0][1])
    final_range = []
    for next_range in ranges[1:]:
        next_low = int(next_range[0])
        next_high = int(next_range[1])
        current_low = temp_range[0]
        current_high = temp_range[1]

        # No Overlap -> we can add the temp_range
        if current_high < next_low:
            final_range.append(temp_range)
            temp_range = (next_low, next_high)
            continue

        # Checking complete overlap
        if current_low >= next_low and current_high <= next_high:
            temp_range = (next_low, next_high)
            continue

        # Checking partial overlap
        if current_low <= next_low and next_low <= current_high <= next_high:
            temp_range = (current_low, next_high)
            continue
        if next_low <= current_low <= next_high and current_high > next_high:
            temp_range = (next_low, current_high)
            continue

    final_range.append(temp_range)
    return final_range

def is_valid_id(id: int, valid_id_ranges: set[tuple[int, int]]) -> bool:
    for valid_range in valid_id_ranges:
        if valid_range[0] <= id <= valid_range[1]:
            return True

    return False

def get_valid_count(id_list: list[str], valid_id_ranges: set[tuple[int, int]]) -> int:
    valid_count = 0

    for id in id_list:
        valid_count += 1 if is_valid_id(int(id), valid_id_ranges) else 0

    return valid_count

# take the first range and see if it overlaps with any other ranges
#   if it does, merge them and remove the other range
#   continue until no more overlaps exist
def cleanup_ranges(ranges: set[tuple[int, int]]) -> set[tuple[int, int]]:
    pass

def main():
    data = FileUtil.read_file('./inputs/day5.txt')

    range_input = []
    id_input = []
    insert_into_range = True
    for line in data:
        if line.strip() == "":
            insert_into_range = False
            continue

        if insert_into_range:
            range_input.append(line)
        else:
            id_input.append(line)

    # P1
    valid_id_ranges = create_valid_id_set(range_input)
    valid_count = get_valid_count(id_input, valid_id_ranges)
    print(f"P1 - Number of valid IDs: {valid_count}")

    # P2
    valid_id_count = 0
    valid_range_list = create_valid_id_list(range_input)
    for valid_range in valid_range_list:
        temp_count = valid_range[1] - valid_range[0] + 1
        valid_id_count += temp_count

    print(f"P2 = {valid_id_count}")

if __name__ == "__main__":
    main()
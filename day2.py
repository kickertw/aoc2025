def create_ranges(input: str) -> list[tuple[int, int]]:
    ranges = []
    parts = input.split(',')
    for part in parts:
        start_str, end_str = part.split('-')
        start, end = int(start_str), int(end_str)
        ranges.append((start, end))
    return ranges

def generate_invalid_ids(min: int, max: int) -> set[int]:
    invalid_ids = set()
    min_range_len = len(str(min))
    
    if min_range_len % 2 != 0:
        min_range_len += 1

    starting_number = 10 ** (min_range_len // 2 - 1)
    while True:
        temp_num = str(starting_number) + str(starting_number)
        temp_num_int = int(temp_num)

        if temp_num_int >= min and temp_num_int <= max:
            invalid_ids.add(temp_num_int)

        if temp_num_int > max:
            break

        starting_number += 1
    
    return invalid_ids

def generate_invalid_ids_v2(min: int, max: int) -> set[int]:
    invalid_ids = set()

    starting_number = 1    
    while True:
        temp_num = str(starting_number)
        while True:
            temp_num += str(starting_number)
            temp_num_int = int(temp_num)

            if temp_num_int < min:
                continue

            if temp_num_int > max:
                break

            if temp_num_int >= min and temp_num_int <= max:
                invalid_ids.add(temp_num_int)

        starting_number += 1
        if int(str(starting_number) * 2) > max:
            break
    
    return invalid_ids

def main():
    #input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    input = "1090286-1131879,3259566-3404881,138124-175118,266204727-266361099,16765-24272,7657360692-7657593676,88857504-88926597,6869078-6903096,48444999-48532270,61427792-61580535,71-103,8077-10421,1920-2560,2-17,951-1259,34-50,28994-36978,1309-1822,9393918461-9393960770,89479-120899,834641-988077,5389718924-5389797353,34010076-34214499,5063-7100,607034-753348,19098586-19261191,125085556-125188689,39839-51927,3246-5037,174-260,439715-473176,187287-262190,348-535,58956-78301,4388160-4505757,512092-584994,13388753-13534387"

    ranges = create_ranges(input)

    invalid_ids = set()
    invalid_ids_v2 = set()
    for min_max in ranges:
        ids = generate_invalid_ids(min_max[0], min_max[1])
        ids_v2 = generate_invalid_ids_v2(min_max[0], min_max[1])

        # if (len(ids) > 0):
        #     print(f"Invalid IDs between {min_max[0]} and {min_max[1]}: {ids}")
        # else:
        #     print(f"No invalid IDs between {min_max[0]} and {min_max[1]}")

        invalid_ids = invalid_ids.union(ids)

        # if (len(ids_v2) > 0):
        #     print(f"Invalid IDs between {min_max[0]} and {min_max[1]}: {ids_v2}")
        # else:
        #     print(f"No invalid IDs between {min_max[0]} and {min_max[1]}")  
        invalid_ids_v2 = invalid_ids_v2.union(ids_v2)        

    sum_of_ids = sum(invalid_ids)
    print(f"Sum of invalid IDs == {sum_of_ids}")

    sum_of_ids_v2 = sum(invalid_ids_v2)
    print(f"Sum of invalid IDs (v2) == {sum_of_ids_v2}")
    return

if __name__ == "__main__":
    main()
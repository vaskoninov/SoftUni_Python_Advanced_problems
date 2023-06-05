def create_sequence(count):
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]

    nums = [0, 1]
    for num in range(2, count):
        next_num = nums[-1] + nums[-2]
        nums.append(next_num)

    return nums


def locate_num(num, seq):
    try:
        index = seq.index(num)
        return f"The number {num} is at index {index}"
    except ValueError:
        return f"the number {num} is not in the sequence"

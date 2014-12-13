
def count_evens(nums):
    return len([x for x in range(len(nums)) if not x % 2])

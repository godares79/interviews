# https://leetcode.com/problems/two-sum/
import collections
import sys


def twosum_exact(nums: list[int], target: int) -> list[int] | None:
    """Find the indexes of the two numbers that add up to the target."""
    if not nums or len(nums) == 1:
        return None

    num_dict: dict[int, list[int]] = collections.defaultdict(list)
    for index, num in enumerate(nums):
        num_dict[num].append(index)
    for number, indexes in num_dict.items():
        difference = target - number
        if num_dict.get(difference, None):
            if number == difference and len(indexes) == 1:
                # If we find the same number to add up to the target, but it's
                # the only instance in the array, then just continue.
                continue
            elif number == difference and len(indexes) > 1:
                # If we find the same number to add up to the target and there
                # is more than one instance in the array, return index 0 and 1.
                return [indexes[0], indexes[1]]
            else:
                # Normal case, just return the two number indexes. Don't need to
                # do a bounds check here because they are unequal.
                return [indexes[0], num_dict[difference][0]]
    return None


def twosum_closest(nums: list[int], target: int) -> list[int] | None:
    """Find the two numbers that are closest/equal to the target.

    Unlike in the exact match, can't use a dict for this. Instead, it's slower.
    Need to sort the list, then work inwards from both ends until finding the
    match or finding the closest.

    Also, it doesn't make sense to return the index of the two values here.
    Instead, return the two values themselves. I guess I could keep a mapping
    of sorted order back to the original order if I really need to return the
    index.
    """
    if not nums or len(nums) == 1:
        return None

    nums.sort()
    lower_index = 0
    upper_index = len(nums) - 1
    lowest_diff = sys.maxsize * 2  # Just make it really big initially
    lowest_diff_values = []
    while lower_index < upper_index:
        sum = nums[lower_index] + nums[upper_index]
        difference = abs(target - sum)
        if difference < lowest_diff:
            lowest_diff = difference
            lowest_diff_values = [nums[lower_index], nums[upper_index]]
        if sum < target:
            lower_index += 1
        elif sum > target:
            upper_index -= 1
        else:
            # Means sum == target, so just return immediately.
            return lowest_diff_values
    return lowest_diff_values


def nsum_exact(nums: list[int], target: int) -> list[int] | None:
    """Return the indexes of all values that sum up to exactly target.

    Each value can only be used once. Can use any number of values from 1 to
    len(nums).
    """
    pass


if __name__ == "__main__":
    print("Two Sum (Exact):")
    print(twosum_exact([2, 7, 11, 15], 9))
    print(twosum_exact([3, 2, 4], 6))
    print(twosum_exact([3, 3], 6))
    print(twosum_exact([], -1))
    print(twosum_exact([1, 1], 11))
    print(twosum_exact([1, -1, 7, -2], 0))

    print("\nTwo Sum (Closest):")
    print(twosum_closest([2, 7, 11, 15], 9))
    print(twosum_closest([3, 2, 4], 6))
    print(twosum_closest([3, 3], 6))
    print(twosum_closest([], -1))
    print(twosum_closest([1, 1], 11))
    print(twosum_closest([1, -1, 7, -2], 0))
    print(twosum_closest([2, 7, 9, 15, 22, 23], 28))

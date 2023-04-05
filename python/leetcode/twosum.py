# https://leetcode.com/problems/two-sum/
import collections


def twosum_exact(nums: list[int], target: int) -> list[int] | None:
    """Find the indexes of the two numbers that add up to the target."""
    if not nums:
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
    """Find the indexes of two numbers that are closest/equal to the target."""
    pass


if __name__ == "__main__":
    print(twosum_exact([2, 7, 11, 15], 9))
    print(twosum_exact([3, 2, 4], 6))
    print(twosum_exact([3, 3], 6))
    print(twosum_exact([], -1))
    print(twosum_exact([1, 1], 11))
    print(twosum_exact([1, -1, 7, -2], 0))

# https://leetcode.com/problems/climbing-stairs/


MemoStore: dict[int, int] = {}


def climbing_stairs(n: int):
    # This is pretty straightforward, in fact it's pretty much just
    # fibonnaci.
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n - 1 in MemoStore:
        left = MemoStore[n - 1]
    else:
        left = climbing_stairs(n - 1)
        MemoStore[n - 1] = left
    if n - 2 in MemoStore:
        right = MemoStore[n - 2]
    else:
        right = climbing_stairs(n - 2)
        MemoStore[n - 2] = right

    return left + right


if __name__ == "__main__":
    print("Climbing up some stairs")
    print("{} Stairs = {} Ways".format(250, climbing_stairs(250)))

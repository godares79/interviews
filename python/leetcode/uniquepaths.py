# https://leetcode.com/problems/unique-paths/

results_store: list[list[int]]


def _init_results_store(m: int, n: int):
    global results_store
    results_store = [[0] * n for _ in range(m)]


def unique_paths(m: int, n: int) -> int:
    if m == 0:
        return 0
    if n == 0:
        return 0
    if m == 1 and n == 1:
        return 0
    if m == 1 and n == 2:
        return 1
    if m == 2 and n == 1:
        return 1

    # The indexes here are kind of a pain, there is probably a better way.
    if not results_store[m - 2][n - 1]:
        results_store[m - 2][n - 1] = unique_paths(m - 1, n)
    if not results_store[m - 1][n - 2]:
        results_store[m - 1][n - 2] = unique_paths(m, n - 1)

    return results_store[m - 2][n - 1] + results_store[m - 1][n - 2]


if __name__ == "__main__":
    _init_results_store(2, 2)
    print(unique_paths(2, 2))
    _init_results_store(3, 7)
    print(unique_paths(3, 7))
    _init_results_store(3, 2)
    print(unique_paths(3, 2))
    _init_results_store(10, 10)
    print(unique_paths(10, 10))
    _init_results_store(11, 11)
    print(unique_paths(11, 11))
    _init_results_store(100, 100)
    print(unique_paths(100, 100))

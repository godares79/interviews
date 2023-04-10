# https://leetcode.com/problems/coin-change/
# Asks for the "fewest number of coins" and it's not guaranteed we can actually
# make the value. Because we can't guarantee we have a set of coins that can
# optimally make the value, we can't use a greedy algorithm line in real life.
# For example, given [3, 5] and an amount of 9. A greedy algo wouldn't work.
# Instead, need to use dynamic programming.


# Key is the amount, value is the minimal number of coins to make that amount.
MemoStore: dict[int, int] = {}


def coin_change(coins: list[int], amount: int) -> int:
    """Returns the fewest number of coins needed to make up the amount.

    If that amount of money cannot be made up by any combination of the coins,
    return -1.
    """
    # Base case. If the amount is 0, then just return 0.
    if amount == 0:
        return 0

    if amount in MemoStore:
        return MemoStore[amount]

    number_of_coins = []
    for coin in coins:
        if coin <= amount:
            coin_count = 1 + coin_change(coins, amount - coin)
            if coin_count > 0:
                number_of_coins.append(coin_count)

    if not number_of_coins:
        return -1
    min_coins = min(number_of_coins)
    MemoStore[amount] = min_coins
    return min_coins


if __name__ == "__main__":
    print("Coin change question")

    MemoStore.clear()
    print(coin_change([1, 2, 5], 11))
    MemoStore.clear()
    print(coin_change([3, 5], 9))
    MemoStore.clear()
    print(coin_change([2, 1], 3))
    MemoStore.clear()
    print(coin_change([1], 0))
    MemoStore.clear()
    print(coin_change([], 1))
    MemoStore.clear()
    print(coin_change([2], 1))
    MemoStore.clear()
    print(coin_change([5, 1, 15], 25))

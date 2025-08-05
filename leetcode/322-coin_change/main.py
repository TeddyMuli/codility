class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        result = 0

        coins.sort()
        for coin in reversed(coins):
            result += amount // coin
            if result == 0:
                continue
            amount = amount % coin
            if amount == 0:
                return result

        return -1

if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5, 6, 12]
    print(sol.coinChange(coins, 11))

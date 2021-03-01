def nonConstructibleChange(coins):
    sum_coins = sum(coins)
    set_coins = list(set(coins))
    set_coins.sort()




    print(sum_coins, set_coins)
    return 1


coins = [5, 7, 1, 1, 2, 3, 22]
nonConstructibleChange(coins)
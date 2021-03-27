def minimumWaitingTime(queries):
    total = 0
    big_total = 0
    queries.sort()
    queries.pop(-1)
    for num in queries:
        total += num
        big_total += total
    return big_total


queries = [3, 2, 1, 2, 6]
answer = minimumWaitingTime(queries)
print(answer)
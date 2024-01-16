def assign_cookies(greed, size):
    greed.sort()
    size.sort()
    g = 0
    s = 0
    count = 0
    while g < len(greed) and s < len(size):
        if greed[g] <= size[s]:
            g += 1
            count += 1
        s += 1
    return count


size = [1, 2, 3, 5]
greed = [5, 6, 7, 8]

result = assign_cookies(greed, size)
print(result)

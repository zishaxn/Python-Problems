def uniqueOccurrences(arr):
    freq_map = {}
    for key in arr:
        if key in freq_map:
            freq_map[key] += 1
        else:
            freq_map[key] = 1

    occurrences_set = set()
    for occur in freq_map.values():
        if occur not in occurrences_set:
            occurrences_set.add(occur)
        else:
            return False

    return True


# Example usage:
arr = [11, 12, 12, 11, 11, 13]
result = uniqueOccurrences(arr)
print(result)

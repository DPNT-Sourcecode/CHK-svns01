

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }
    for char in skus:
        if not char in counts.keys():
            return -1
        counts[char] += 1

    sum = 0
    sum += (counts['A'] // 3) * 130 + (counts['A'] % 3) * 50
    sum += (counts['B'] // 2) * 45 + (counts['B'] % 2) * 30
    sum += counts['C'] * 20
    sum += counts['D'] * 15

    return sum 


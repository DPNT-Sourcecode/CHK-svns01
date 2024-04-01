

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
    }
    for char in skus:
        if not char in counts.keys():
            return -1
        counts[char] += 1

    free_items = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
    }

    # For now, will always be cheaper to deduct the free item
    counts['B'] = max(counts['B'] - counts['E'] // 2, 0)

    sum = 0

    sum += (counts['A'] // 5) * 200
    counts['A'] = counts['A'] % 5
    sum += (counts['A'] // 3) * 130
    counts['A'] = counts['A'] % 3
    sum += counts['A'] * 50

    sum += (counts['B'] // 2) * 45 + (counts['B'] % 2) * 30
    sum += counts['C'] * 20
    sum += counts['D'] * 15
    sum += counts['E'] * 40

    return sum 

checkout("EE")
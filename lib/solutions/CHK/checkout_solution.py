

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = {k: 0 for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    for char in skus:
        if not char in counts.keys():
            return -1
        counts[char] += 1

    # For now, will always be cheaper to deduct the free item
    counts['B'] = max(counts['B'] - counts['E'] // 2, 0)

    counts['F'] = max(counts['F'] - counts['F'] // 3, 0)

    counts['M'] = max(counts['M'] - counts['N'] // 3, 0)

    counts['Q'] = max(counts['Q'] - counts['R'] // 3, 0)

    counts['U'] = max(counts['U'] - counts['U'] // 4, 0)

    sum = 0

    sum += triple_price(counts['A'], 50, 3, 130, 5, 200)

    sum += double_price(counts['B'], 30, 2, 45)

    sum += counts['C'] * 20
    sum += counts['D'] * 15
    sum += counts['E'] * 40
    sum += counts['F'] * 10
    sum += counts['G'] * 20

    sum += triple_price(counts['H'], 10, 5, 45, 10, 80)

    sum += counts['I'] * 35
    sum += counts['J'] * 60
    
    sum += double_price(counts['K'], 70, 2, 120)

    sum += counts['L'] * 90

    sum += counts['M'] * 15
    sum += counts['N'] * 40 
    sum += counts['O'] * 10
    
    sum += double_price(counts['P'], 50, 5, 200)
    
    sum += double_price(counts['Q'], 30, 3, 80)

    sum += counts['R'] * 50
    sum += counts['S'] * 20
    sum += counts['T'] * 20
    sum += counts['U'] * 40
    
    sum += triple_price(counts['V'], 50, 2, 90, 3, 130)

    sum += counts['W'] * 20
    sum += counts['X'] * 17
    sum += counts['Y'] * 20
    sum += counts['Z'] * 21

    return sum 


def double_price(count, base_price, volume1, price1):
    return (count // volume1) * price1 + (count % volume1) * base_price

def triple_price(count, base_price, volume1, price1, volume2, price2):
    sum = 0
    sum += (count // volume2) * price2
    count = count % volume2
    sum += (count // volume1) * price1
    count = count % volume1
    sum += count * base_price
    return sum


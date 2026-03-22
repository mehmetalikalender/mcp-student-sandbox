def average_ratios(numbers):
    total = 0.0
    valid_count = 0

    for number in numbers:
        if number == 0:
            # Skip zero values to avoid division by zero.
            continue
        total += 100 / number
        valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count

print(average_ratios([10, 5, 0]))

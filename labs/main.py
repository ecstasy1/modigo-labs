def second_largest(numbers):
    # TODO: return the second largest DISTINCT number in `numbers`
    unique = set(numbers)
    return sorted(unique,reverse=True)[1]
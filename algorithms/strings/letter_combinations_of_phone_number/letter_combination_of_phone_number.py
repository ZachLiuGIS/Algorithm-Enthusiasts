def get_combinations(digits):
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': [' '],
    }

    results = []

    def update_digit(lst):
        new_lst = []
        if lst:
            for item in mapping[d]:
                for result in lst:
                    new_lst.append(result + item)
        else:
            new_lst = mapping[d]
        return new_lst

    for d in digits:
        results = update_digit(results)

    return results

print(get_combinations('2'))

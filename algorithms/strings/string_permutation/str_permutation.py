import cProfile


def str_permutation(str_):
    permutations = []

    def get_permutation(s, prefix):
        if len(s) == 0:
            permutations.append(prefix)
        else:
            for i, c in enumerate(s):
                get_permutation(s[:i] + s[i+1:], prefix + c)

    get_permutation(str_, '')

    return permutations


if __name__ == '__main__':
    print(str_permutation('abcdefg'))
    cProfile.run('str_permutation("abcdefghijk")')


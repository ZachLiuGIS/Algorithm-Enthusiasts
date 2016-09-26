def substring_with_concatenation_of_all_words_brute_force(s, words):
    ret = []
    len_s = len(s)
    len_w = len(words[0])
    len_ws = len_w * len(words)

    def is_combination(s_):
        i = 0
        words_copy = words[:]
        while i < len(s_):
            if s_[i:i + len_w] in words_copy:
                words_copy.remove(s_[i:i + len_w])
            else:
                return False
            i += len_w
        return True

    for i in range(len_s - len_ws + 1):
        if is_combination(s[i:i + len_ws]):
            ret.append(i)

    return ret


def substring_with_concatenation_of_all_words(s, words):
    ret = []
    len_s = len(s)
    len_w = len(words[0])
    len_ws = len_w * len(words)
    if len_s < len_ws:
        return ret

    lookup = {}
    for word in words:
        if word not in lookup:
            lookup[word] = 1
        else:
            lookup[word] += 1

    index = 0
    while index < len_w:
        i = index
        counter = 0
        start = index
        hash_word = {}

        while i < len_s:
            tmp_w = s[i:i+len_w]
            if tmp_w not in lookup:
                counter = 0
                start = i + len_w
                hash_word = {}

            elif tmp_w in hash_word and hash_word[tmp_w] == lookup[tmp_w]:
                hash_word[s[start:start + len_w]] -= 1
                start += len_w
                counter -= 1
                continue

            elif tmp_w not in hash_word:
                hash_word[tmp_w] = 1
                counter += 1
            else:
                hash_word[tmp_w] += 1
                counter += 1

            if counter == len(words):
                ret.append(start)
                hash_word[s[start:start + len_w]] -= 1
                start += len_w
                counter -= 1
            i += len_w
        index += 1
    return ret

if __name__ == '__main__':
    assert substring_with_concatenation_of_all_words_brute_force("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    print(substring_with_concatenation_of_all_words("barfoothefoobarman", ["foo", "bar"]))

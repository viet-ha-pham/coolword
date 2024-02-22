def segoholin(word):

    # Special case:
    if len(word) == 1:
        if word == "a":
            return "e"
        if word == "e":
            return "i"
        if word == "i":
            return "o"
        if word == "o":
            return "u"
        if word == "u":
            return "i"
        return word

    vowels = "aeiouy"

    a = [ c for c in word if c not in vowels]
    a.sort()

    b = [ c for c in word if c in vowels]
    b.sort()

    m = min(len(a), len(b))
    i = 0
    new_word = ""

    if len(a) >= len(b):
        while i < m:
            new_word += a[i]
            new_word += b[i]
            i += 1
        if i < len(a) and a[i] in "mnprst":
            new_word += a[i]
    else:
        while i < m:
            new_word += b[i]
            new_word += a[i]
            i += 1
        if i < len(b):
            new_word += b[i]

    # Post processing
    if new_word == word:
        new_word = new_word[::-1]
    if new_word[-1] not in "mnprst":
            new_word = new_word[:len(new_word) - 1] + "t"

    return new_word.replace("y","i").replace("c","s")


def yoohet(word1, word2):
    rev_word1 = word1[::-1]
    rev_word2 = word2[::-1]

    common_index = None
    for i in range(len(rev_word2)):
        for j in range(len(rev_word1)):
            if rev_word2[i] == rev_word1[j]:
                common_index = (i, j)

    if common_index == None:
        return rev_word2[:len(rev_word2)//2] + rev_word1[:len(rev_word1)//2]

    return rev_word2[:common_index[0]] + rev_word1[common_index[1]:]


if __name__ == '__main__':
    print(segoholin("technology"))
    print(yoohet("technology","chwinrwang"))
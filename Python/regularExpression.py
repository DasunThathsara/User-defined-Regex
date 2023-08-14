def traverse(String, Pattern, breaking_point, pi):
    if breaking_point > len(String) - len(Pattern):
        return False

    q = 0
    for i in range(len(Pattern)):
        if String[i + breaking_point] != Pattern[i]:
            break
        q += 1

    if q == len(Pattern):
        return True

    if q == 0:
        return traverse(String, Pattern, breaking_point + 1, pi)

    return traverse(String, Pattern, breaking_point + (q - pi[q - 1][1]), pi)

def kmp(String, Pattern):
    pi = []
    for i in range(len(Pattern) + 1):
        postfix = []
        prefix = []
        maxLength = 0

        sub = "".join(Pattern[: i])
        for j in range(1, i):
            prefix.append(sub[: j])
            postfix.append(sub[i - j:])

        for j in range(len(prefix)):
            if prefix[j] in postfix:
                if len(prefix[j]) > maxLength:
                    maxLength = len(prefix[j])

        if i != 0:
            pi.append([Pattern[i - 1], maxLength])

    return traverse(String, Pattern, 0, pi)


def search(String, Pattern):
    # --------------------- Find Either Or relation --------------------
    if any(i == '|' for i in Pattern):
        return search(String, Pattern.split('|')[0]) or search(String, Pattern.split('|')[1])

    # ---- Find if String starts with Pattern and ends with Pattern ----
    elif any(i == '?' for i in Pattern):
        if Pattern[-1] == '?':
            return search(String, Pattern.split('?')[0]) or search(String, Pattern.split('?')[0][:len(Pattern.split('?')[0]) - 1])
        elif Pattern[0] == '?':
            return search(String, Pattern.split('?')[1]) or search(String, Pattern.split('?')[1][1:])
        else:
            return search(String, Pattern.split('?')[0][-1] + Pattern.split('?')[1][0]) or search(String, Pattern.split('?')[0][-1][:len(Pattern.split('?')[0][-1]) - 1] + Pattern.split('?')[1][0])

    # ---- Find if String starts with Pattern and ends with Pattern ----
    elif Pattern[0] == "^" and Pattern[-1] == "$":
        return kmp(String, "".join(Pattern[1: len(Pattern) - 1])) and len(String) == len(Pattern) - 2

    # --------------- Find if String starts with Pattern ---------------
    elif Pattern[0] == "^":
        return kmp(String[: len(Pattern) - 1], "".join(Pattern[1:]))

    # ---------------- Find if String ends with Pattern ----------------
    elif Pattern[-1] == "$":
        return kmp(String[len(String) - len(Pattern) + 1:], "".join(Pattern[0: len(Pattern) - 1])) and search(String, "".join(Pattern[:len(Pattern) - 1]))

    return kmp(String, Pattern)
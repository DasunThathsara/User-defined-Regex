def build_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = 0
    j = 0
    matches = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def regex_search(text, pattern):
    if '|' in pattern:
        parts = pattern.split('|')
        return regex_search(text, parts[0]) or regex_search(text, parts[1])

    elif pattern.startswith('^') and pattern.endswith('$'):
        matches = kmp_search(text, pattern[1:len(pattern) - 1])

        if 0 in matches:
            return [0]
        else:
            return []

    elif pattern.startswith('^'):
        matches = kmp_search(text, pattern[1:])

        if 0 in matches:
            return [0]
        else:
            return []

    elif pattern.endswith('$'):
        matches = kmp_search(text, pattern[:-1])

        if len(text) - len(pattern) + 1 in matches:
            return [len(text) - len(pattern) + 1]
        else:
            return []

    else:
        return kmp_search(text, pattern)


def search_in_file(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    output = []

    line_num = 1
    for line in lines:
        matches = regex_search(line.strip(), open(pattern, 'r').read().strip())
        if matches:
            output.append(f"Line {line_num}, Position(s): {', '.join(map(str, matches))}")

        line_num += 1
    return output


def main():
    file_path = "test cases/text.txt"
    pattern = "test cases/pattern.txt"

    output = search_in_file(file_path, pattern)

    output_file_path = "output.txt"
    with open(output_file_path, 'w') as output_file:
        if output:
            output_file.write("\n".join(output))
            print(f"Matches found. Results saved to '{output_file_path}'.")
        else:
            output_file.write("No matches found.")
            print("No matches found.")


if __name__ == "__main__":
    main()

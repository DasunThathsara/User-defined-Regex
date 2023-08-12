import regularExpression as re

# Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
#        $ - ends with. ex:- abc$ - given string ends with abc
#        ^ - starts with. ex:- ^abc - given string starts with abc
#        | - or. ex:- a|b - given string contains a or b

if __name__ == '__main__':
    text = open("test cases/text.txt", 'r')
    pattern = open("test cases/pattern.txt", 'r')
    output = open("results/patternmatch.output", 'w')

    String = text.readline().strip()
    Pattern = pattern.readline().strip()

    output.writelines(str(re.search(String, Pattern)))

    text.close()
    pattern.close()
    output.close()
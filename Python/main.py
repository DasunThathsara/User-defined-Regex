import regularExpression as re

# Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
#        $ - ends with. ex:- abc$ - given string ends with abc
#        ^ - starts with. ex:- ^abc - given string starts with abc
#        | - or. ex:- a|b - given string contains a or b


if __name__ == '__main__':
    f = open("test cases/text1.txt", 'r')
    print("String:", f.readline().strip())
    print("Pattern:", f.readline())

    String = input("Enter String: ")
    Pattern = input("Enter Pattern: ")

    print(re.search(String, Pattern))
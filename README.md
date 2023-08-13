# User-Defined Regex
Implement Regex characters using the Knuth-Morris-Pratt (KMP) string matching algorithm. The solution was done using the Python programming language. 

<br /><br />
## How to run?
First, go to the [python](https://github.com/DasunThathsara/User-defined-Regex/tree/main/Python) folder and find the main.py file. This is the code file in this scenario. You can run it using your own test cases and open the [results](https://github.com/DasunThathsara/User-defined-Regex/tree/main/Python/results) folder to view the outputs. If you want to add a new test case, go to the [test cases](https://github.com/DasunThathsara/User-defined-Regex/tree/main/Python/test%20cases) folder and create your own test case file.


<br />

You can change this text file name to your own file name.
```python
text = open("test cases/text.txt", 'r')
pattern = open("test cases/pattern.txt", 'r')
output = open("results/patternmatch.output", 'w')
```

`regularExpression.py` contains the Regex file, and the main file imports functions from the `regularExpression.py` file.
<br/><br/>
#
First, import `regularExpression.py` and set the alias to re. Because `regularExpression` is too long and hard to handle.
```python
import regularExpression as re
```

<br /><br />

## Methodology
I use the `Knuth-Morris-Pratt (KMP)` algorithm to implement this and filter the pattern using simple if statements. Also, the matiching condition is called to the relevant function, and the output is given as a Boolean value.

```python
def search(String, Pattern):
    # --------------------- Find Either Or relation --------------------
    if any(i == '|' for i in Pattern):
        return search(String, Pattern.split('|')[0]) or search(String, Pattern.split('|')[1])

    # ---- Find if String starts with Pattern and ends with Pattern ----
    elif Pattern[0] == "^" and Pattern[-1] == "$":
        return start_with_and_ends_with(String, Pattern)

    # --------------- Find if String starts with Pattern ---------------
    elif Pattern[0] == "^":
        return start_with(String, Pattern)

    # ---------------- Find if String ends with Pattern ----------------
    elif Pattern[-1] == "$":
        return ends_with(String, Pattern)

    # ----- This part runs if the upper parts was not saticefied -------
    return kmp(String, Pattern)
```

In this version, the program recognizes `^` `|` `$` as the regex character.


____
<p align="center">
    <a href="https://github.com/UltiRequiem/python-projects-for-intermediates/blob/main/LICENSE">
      <img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
    </a
    &nbsp;
    <a href="https://hits.sh/github.com/DasunThathsara/User-defined-Regex/">
      <img alt="Hits" src="https://hits.sh/github.com/DasunThathsara/User-defined-Regex.svg?label=Views"/>
    </a>
    <a href="https://github.com/DasunThathsara/User-defined-Regex/actions">
      <img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg" />
    </a>
    <a href="https://github.com/DasunThathsara/User-defined-Regex/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/DasunThathsara/User-defined-Regex" />
    </a>
    <a href="https://github.com/DasunThathsara/User-defined-Regex/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/DasunThathsara/User-defined-Regex?color=0088ff" />
    </a>
    <a href="https://github.com/DasunThathsara/User-defined-Regex/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/DasunThathsara/User-defined-Regex?color=0088ff" />
    </a>
  </p>

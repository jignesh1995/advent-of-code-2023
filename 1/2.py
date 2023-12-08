f = open("input.txt", "r+")
import re
sum = 0
wordnumbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def toDigit(character):
    if character in numbers:
        return int(character)
    else:
        return wordnumbers.index(character)
    

for line in f:
    regex = r"one|two|three|four|five|six|seven|eight|nine|zero|0|1|2|3|4|5|6|7|8|9"
    regexrev = r"9|8|7|6|5|4|3|2|1|0|orez|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno"

    first = re.search(regex, line).group(0)

    second = re.search(regex[::-1], line[::-1]).group(0)
    print(first, second)
    # print(second)
    sum += ((toDigit(first) * 10) + toDigit(second[::-1]))
    

print("maxSum=", sum)

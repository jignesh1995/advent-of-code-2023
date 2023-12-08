f = open("input.txt", "r+")

sum = 0
wordnumbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def isDigit(character):
    return character in numbers
    

for line in f:
    for index, word in enumerate(wordnumbers):
        line=line.replace(word, numbers[index])

    # print(line)
    lineArr = [*line]
    first = 0
    second = 0
    for charx in lineArr:
        if isDigit(charx):
            first = int(charx)
            break
    lineArr.reverse()
    for chary in lineArr:
        if isDigit(chary):
            second = int(chary)
            break
    sum += ((first * 10) + second)
    

print("maxSum=", sum)

f = open('./input.txt', 'r+')
import re
mapping = list()
symbol = r'[^\d\.A-Za0z\s]{1}'
period = r'\.+'
digit = r'\d+'
def createMap():
  index = -1
  for line in f:
    index += 1
    mapping.append(list())
    print(period, line)
    for match in re.finditer(period, line):
      print(match)
      mapping[index].append({'start': match.start(), 'end': match.end(), 'match': '.', 'type': 'period', 'select': False})
    for match in re.finditer(digit, line):
      mapping[index].append({'start': match.start(), 'end': match.end(), 'match': match[0], 'type': 'number', 'select': False})
    for match in re.finditer(symbol, line):
      mapping[index].append({'start': match.start(), 'end': match.end(), 'match': match[0], 'type': 'symbol', 'select': False})
    # mapping[index].sort(key=lambda x: x['start'])

  return mapping

createMap()
numbersToAdd = []
sumOfNumbers = 0

for rowIndex, row in enumerate(mapping):
  for data in row:
    print('data=', data)
    if data['type'] == 'symbol' != None:
      # Symbol found
      if rowIndex == 0:
        # check curr and curr + 1
        print(rowIndex)
        # check curr
        for ele in row:
          if ele['type'] == 'number' and ele['select'] == False and (ele['end'] == data['start'] or ele['start'] == data['end']):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
        # check next element
        for ele in mapping[rowIndex + 1]:
          if ele['type'] == 'number' and ele['select'] == False and ((ele['start'] <= data['start'] <= ele['end']) or (ele['start'] <= data['end'] <= ele['end'])):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
      elif rowIndex == len(mapping) - 1:
        # last row, check curr and curr - 1
        print(rowIndex)
        # check curr
        for ele in row:
          if ele['type'] == 'number' and ele['select'] == False and (ele['end'] == data['start'] or ele['start'] == data['end']):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
        # check prev element
        for ele in mapping[rowIndex - 1]:
          if ele['type'] == 'number' and ele['select'] == False and ((ele['start'] <= data['start'] <= ele['end']) or (ele['start'] <= data['end'] <= ele['end'])):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
      else:
        # middle row, check curr - 1, curr and curr + 1
        print(rowIndex)
        # check curr
        for ele in row:
          if ele['type'] == 'number' and ele['select'] == False and (ele['end'] == data['start'] or ele['start'] == data['end']):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
        # check next element
        for ele in mapping[rowIndex + 1]:
          print('ele', ele)
          if ele['type'] == 'number' and ele['select'] == False and ((ele['start'] <= data['start'] <= ele['end']) or (ele['start'] <= data['end'] <= ele['end'])):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])
        # check prev element
        for ele in mapping[rowIndex - 1]:
          if ele['type'] == 'number' and ele['select'] == False and ((ele['start'] <= data['start'] <= ele['end']) or (ele['start'] <= data['end'] <= ele['end'])):
            ele['select'] = True
            sumOfNumbers += int(ele['match'])

print('sumOfNumbers=', sumOfNumbers)
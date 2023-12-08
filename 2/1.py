f = open("input.txt", "r+")
import re
def identifyGames():
  maxRed = 12
  maxGreen = 13
  maxBlue = 14
  sumOfGameIds = 0
  for game in f:
    'Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red'
    sections = game.split(':')
    gameIdSection = sections[0].strip()
    drawsSection = sections[1].strip()
    gameId = int(gameIdSection.strip('Game '))
    draws = drawsSection.split(';')
    gameValid = True
    for draw in draws:
      choices = draw.split(',')
      redCount = 0
      greenCount = 0
      blueCount = 0
      for choice in choices:
        if re.search('red', choice) is not None:
          redCount = int(choice.strip().strip(' red'))
        if re.search('green', choice) is not None:
          greenCount = int(choice.strip().strip(' green'))
        if re.search('blue', choice) is not None:
          blueCount = int(choice.strip().strip(' blue'))
      if redCount > maxRed or greenCount > maxGreen or blueCount > maxBlue:
        gameValid = False
    if gameValid:
      sumOfGameIds += gameId

  return sumOfGameIds

print(identifyGames())



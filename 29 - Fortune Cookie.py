import random

def fortune():
  random_fortune = random.randint(0,3)
  fortunes = ['Dont pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'Someone in your life needs a letter from you.']
  return(fortunes[random_fortune])

print(fortune())
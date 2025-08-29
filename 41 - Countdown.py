import datetime as date
import random as rd


bday_messages = ['Hope you have a very Happy Birthday! 🎈', 
'It\'s your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞']

random_message = rd.choice(bday_messages)

today = date.date.today()
next_birthday = date.date(2026, 8, 4)
days_away = today - next_birthday

if(today == next_birthday):
  print(random_message)
else:
  days_away = abs(days_away.days)
  print(f"My next birthday is {days_away} days away!")
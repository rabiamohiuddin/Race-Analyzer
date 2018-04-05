# Lab 8: report on racing results
from raceAnalyzer import RaceAnalyzer

analyzer = RaceAnalyzer()

print("Total:", analyzer.getCount(), "racers")
menu = ('''Choose from:
  n. search for racer by name
  t. print all result by race type
  l. print count of racers by location
  q. quit
Your choice: ''')
answer = input("\n" + menu).lower()
while answer != 'q':
    if answer == 'n':
        analyzer.searchByName()
    elif answer == 't':
        analyzer.searchByType()
    elif answer == 'l':
        analyzer.searchByLocation()
    elif answer != 'q':
        print("Invalid search type")
    answer = input("\n" + menu).lower()

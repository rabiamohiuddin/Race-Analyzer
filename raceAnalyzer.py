# Lab 8
# Rabia Mohiuddin
# CIS 41A
# Fall 2017

import re

class RaceAnalyzer:
    def __init__(self) :
        ''' Constructor 
            Populates from file
        '''    
        filename = "lab8input.txt"
        self._locationCount = {}                 # Dictionary of racers by location (key)
        self._totalRacers = 0                    # count of total racers
        self._racers = {}                       # Dictionary of all racers with name (key) and list of attributes (value)
        self._raceType = {}                       # Dictionary of all racers with name (key) and list of attributes (value)
        
        self._raceType["50 Mile"] = []        
        self._raceType["100 Mile"] = []
        
        list100o = []
        list100m = []
        list50o = []
        list50m = []        
        
        findme = "\"([^\"]+)\".*, ([A-Za-z]{2}).*\s(\d+ Mile)\s+(\w+).*?\s?(\d+:\d+:\d+.\d|DNF)"
        findme2 = '"([^"]+)".*.\s+(..).*\s(\d+)\s+Mile\s+(Open|Masters)\s+\w+\s+([^\s])'
        
        try:
            with open (filename) as infile:   
                for line in infile:
                    m = re.search(findme2, line)
                    if m:
                        (name, location, distance, category, time) = (m.group(1).title(), m.group(2).upper(), m.group(3), m.group(4).title(), m.group(5))
                                                                 
                        self._locationCount[location] = self._locationCount.get(location, 0) + 1
                        self._totalRacers += 1
                        self._racers[name] = self._racers.get(name, [name, distance, time])
                        
                        if category == "Open" :
                            if distance == "100 Mile" : 
                                list100o.append(name)
                            else :
                                list50o.append(name)
                        elif category == "Masters" :
                            if distance == "100 Mile" : 
                                list100m.append(name)
                            else :
                                list50m.append(name)                            
            
            
            self._raceType["50 Mile"].append(list50o)
            self._raceType["50 Mile"].append(list50m) 
                                
            self._raceType["100 Mile"].append(list100o)
            self._raceType["100 Mile"].append(list100m)
                       
            
        except FileNotFoundError as e :
            print("File not found")
            raise SystemExit
   
    def getCount(self) :
        return self._totalRacers
    
    
    def searchByName(self) :
        nameNotFound = True
        name = input("Enter a racer full name: ").title()
        while nameNotFound:
            try: 
                print("Name: ", self._racers[name][0])
                print("Distance: ", self._racers[name][1])
                print("Time: ", self._racers[name][2])
                print()
                nameNotFound = False
                
            except KeyError as k :
                print("No racer by the name" , name)
                name = input("Enter a racer full name: ").title()
     
    # dummy filler rn   
    def searchByType(self) :
        for distance in sorted(self._raceType):
            print(distance , "distance")
            i = 0                            
            for category in sorted(self._raceType[distance]) :
                if i == 0:
                    subtype = "Open"
                else:
                    subtype = "Masters"
                
                print("  " + subtype)
                for name in sorted(self._raceType[distance][i]) :
                    print(name)
                
                num = len(self._raceType[distance][i])
                print(num , "racers in the" , distance , subtype , "race")
                print()
                i += 1
                
        
    def searchByLocation(self) :
        for state in sorted(self._locationCount):
            print("%s: %d" % (state, self._locationCount[state]))
        
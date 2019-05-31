'''
Created on Nov 13, 2018

@author: arana3 and _______: Aparajita R & Shay M

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
def loaddata():
    database = {}
    try:
        handle = open("musicrecplus.txt", "r")
        lines = handle.read().splitlines()
        handle.close()
        for line in lines:
            name, artists = line.split(':')
            database[name] = sorted(artists.split(','))
    except:
        return database
    return database

def getUser():
    print('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):')
    username = input()
    return username

def Menu():
    print('Enter a letter to choose an option:\n\
e - Enter preferences\nr - Get recommendations\n\
p - Show most popular artists\nh - How popular is the most popular\n\
m - Which user has the most likes\nq - Save and quit')
    choice = input()
    return choice

def getRecs(user, database):
    def compare(userArtists, otherArtists, otherUName):
        if otherUName[-1] == '$':
            return -1
        iUser = 0
        iOther = 0
        score = 0
        while iUser < len(userArtists) and iOther < len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                score += 1
                iUser += 1
                iOther += 1
            elif aUser < aOther:
                iUser += 1
            else:
                iOther += 1
        if len(userArtists) == score:
            return -1
        return score
    def diff(userArtists, otherArtists):
        iUser = 0
        iOther = 0
        diffs = []
        while iUser < len(userArtists) and iOther < len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                iUser += 1
                iOther += 1
            elif aUser < aOther:
                iUser += 1
            else:
                iOther += 1
                diffs.append(aOther)
        if iOther < len(otherArtists):
            diffs.extend(otherArtists[iOther:])
        return diffs
    userArtists = database[user]
    ranked = sorted(myMap(lambda uname: (compare(userArtists, database[uname], uname), uname), database), reverse = True)
    if len(ranked) == 0 or ranked[0][0] == -1:
        print("No recommendations available at this time")
        return
    maxScore = ranked[0][0]
    iMax = 0
    for result in ranked:
        if maxScore != result[0]:
            break
        iMax +=1
    artists = []
    for i in range(iMax):
        artists.extend(diff(userArtists, database[ranked[i][1]]))
    artists = sorted(list(set(artists)))
    printPerLine(artists)

def myMap(fn, iterable):
    ret = [0]*len(iterable)
    i = 0
    for thing in iterable:
        ret[i] = fn(thing)
        i += 1
    return ret

def printPerLine(iterable):
    for thing in iterable:
        print(thing)
        
def addUser(user, database):
    handle = open("musicrecplus.txt", "a+")
    handle.write(user + ':')
    for i in range(len(database[user])) :
        if i == len(database[user])-1:
                handle.write(database[user][i])
        else:
            handle.write(database[user][i] + ',')
    handle.close()

def getPreferences(user, database):
    print("Enter an artist that you like (Enter to finish):")
    pref = input()
    while pref != "":
        database[user] += [pref]
        print("Enter an artist that you like (Enter to finish):")
        pref = input()
    addUser(user, database)

def showPopular(database):
    artistList = sorted(getArtists(database))
    if artistList == []:
        print('Sorry, no artists found.')
    else:
        noDups = []
        for element in artistList:
            if element not in noDups:
                noDups.append(element)
        max_val = artistList.count(noDups[0])
        max_element = noDups[0]
        saveDoubles = []
        for element in noDups:
            occurances = artistList.count(element)
            if occurances > max_val:
                max_val = occurances
                max_element = element
        for element in noDups:
            occurances = artistList.count(element)
            if max_val == occurances:
                saveDoubles += [element]
        if saveDoubles != []:
            printPerLine(sorted(saveDoubles))
        else:
            print(max_element)

def getArtists(database):
        artistList = []
        for key in database:
            if key[-1] == '$':
                continue
            temp = database[key]
            for element in temp:
                if temp.count(element) == 1:
                    artistList.append(element)
                elif temp.count(element) > 1:
                    artistList.append(element)
                    temp = [item for item in temp if item != element]
        return artistList
        
def howPopular(database):
    artistList = sorted(getArtists(database))
    if artistList == []:
        print('Sorry, no artists found.')
    else:
        noDups = []
        for element in artistList:
            if element not in noDups:
                noDups.append(element)
        max_val = artistList.count(noDups[0])
        for element in noDups:
            occurances = artistList.count(element)
            if occurances > max_val:
                max_val = occurances
        print(max_val)

def mostLikedUser(database):
    max_val = 0
    saveDoubles = []
    for key in database:
        if key[-1] == '$':
            continue
        if len(database[key]) > max_val:
            max_val = len(database[key])
    for key in database:
        if key[-1] == '$':
            continue
        if max_val == len(database[key]):
            saveDoubles.append(key)
    if saveDoubles != []:
        printPerLine(sorted(saveDoubles))
    else:
        print(max_val)

def saveAndQuit(database):
    handle = open("musicrecplus.txt", "w")
    for key in database:
        handle.write(key + ':')
        for i in range(len(database[key])):
            if i == len(database[key])-1:
                handle.write(database[key][i])
            else:
                handle.write(database[key][i] + ',')
        handle.write('\n')
    handle.close()
    raise SystemExit
    
def main():
    database = loaddata()
    user = getUser()
    if user not in database:
        database.update({user:[]})
        getPreferences(user, database)
    menuChoice = Menu()
    while menuChoice != 'q':
        if menuChoice ==  'e':
            getPreferences(user, database)
            menuChoice = Menu()
        elif menuChoice == 'r':
            getRecs(user, database)
            menuChoice = Menu()
        elif menuChoice == 'p':
            showPopular(database)
            menuChoice = Menu()
        elif menuChoice == 'h':
            howPopular(database)
            menuChoice = Menu()
        elif menuChoice == 'm':
            mostLikedUser(database)
            menuChoice = Menu()
    saveAndQuit(database)

main()
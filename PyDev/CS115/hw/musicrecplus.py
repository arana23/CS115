'''
Created on Nov 13, 2018

@author: arana3 - Aparajita R
@author: smccart3 -  Shay M

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''


def loaddata():
    #load users, stores values divided into name and artists
    database={}
    try:
        filen=open("musicrecplus.txt", "r")
        lines=filen.read().splitlines()
        filen.close()
        for line in lines:
            name,artists=line.split(':')
            database[name] = sorted(artists.split(','))
    except:
        return database
    return database

def getUser():
    #receives user's name and whether or not $
    print('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):')
    username=input()
    return username

def menu():
    #prints menu options
    print ("e - Enter preferences")
    print ("r - Get recommendations")
    print ("p - Show most popular artists")
    print ("h - How popular is the most popular")
    print ("m - Which user has the most likes")
    print ("q - Save and quit")
    
def getRecs(user, database):
    #check if artist could be a potential recommendation
    def compare(uartists, oartists, otherUName):
        #compare the user input artists, other artists, and then sees potential recs
        if otherUName[-1] == '$':
            return -1
        #keeps track of scores of each 
        iUser=0
        iOther=0
        score=0
        while iUser<len(uartists) and iOther<len(oartists):
            aUser=uartists[iUser]
            aOther=oartists[iOther]
            if aUser == aOther:
                score += 1
                iUser += 1
                iOther += 1
            elif aUser<aOther:
                iUser += 1
            else:
                iOther += 1
        if len(uartists) == score:
            return -1
        return score
    def diff(uartists, otherArtists):
        #which vals are different and accordingly edit iUser and the rest
        iUser = 0
        iOther = 0
        diffs = []
        #comparision of counters
        while iUser < len(uartists) and iOther < len(otherArtists):
            aUser = uartists[iUser]
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
    uartists = database[user]
    ranked = sorted(map(lambda uname: (compare(uartists, database[uname], uname), uname), database), reverse = True)
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
        artists.extend(diff(uartists, database[ranked[i][1]]))
    printeachline(artists)

def printeachline(i):
    #prints out respective lines
    for x in i:
        print(x)

def map(fn, i):
    ret = [0]*len(i)
    c = 0
    for x in i:
        ret[c] = fn(x)
        c += 1
    return ret

def adduser(user,database):
    filen= open("musicrecplus.txt", "a+")
    filen.write(user + ':')
    for i in range(len(database[user])) :
        if i == len(database[user])-1:
                filen.write(database[user][i])
        else:
            filen.write(database[user][i] + ',')
    filen.close()

def getPreferences(user, database):
    print("Enter an artist that you like (Enter to finish):")
    pref = input()
    while pref != "":
        database[user] += [pref]
        print("Enter an artist that you like (Enter to finish):")
        pref = input()
    adduser(user, database)

def getartists(database):
        artistlist = []
        for key in database:
            if key[-1] == '$':
                continue
            temp = database[key]
            for element in temp:
                if temp.count(element) == 1:
                    artistlist.append(element)
                elif temp.count(element) > 1:
                    artistlist.append(element)
                    temp = [item for item in temp if item != element]
        return artistlist

def showPopular(database):
    artistList = sorted(getartists(database))
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
            printeachline(sorted(saveDoubles))
        else:
            print(max_element)
            
def howPopular(database):
    artistList = sorted(getartists(database))
    if artistList == []:
        print('Sorry, no artists found.')
    else:
        dup = []
        for element in artistList:
            if element not in dup:
                dup.append(element)
        max_val = artistList.count(dup[0])
        for element in dup:
            occurances = artistList.count(element)
            if occurances > max_val:
                max_val = occurances
        print(max_val)

def mostLikedUser(database):
    maxv= 0
    sdoub = []
    for key in database:
        if key[-1] == '$':
            continue
        if len(database[key]) > maxv:
            maxv = len(database[key])
    for key in database:
        if key[-1] == '$':
            continue
        if maxv == len(database[key]):
            sdoub.append(key)
    if sdoub != []:
        printeachline(sorted(sdoub))
    else:
        print(maxv)

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
    menuChoice = menu()
    while menuChoice != 'q':
        if menuChoice ==  'e':
            getPreferences(user, database)
            menuChoice = menu()
        elif menuChoice == 'r':
            getRecs(user, database)
            menuChoice = menu()
        elif menuChoice == 'p':
            showPopular(database)
            menuChoice = menu()
        elif menuChoice == 'h':
            howPopular(database)
            menuChoice = menu()
        elif menuChoice == 'm':
            mostLikedUser(database)
            menuChoice = menu()
    saveAndQuit(database)

main()
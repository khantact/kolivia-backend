import spacy
from datetime import date
from dateInfo import monthsofYear, daysOfTheWeekAsStrs, months


def isMonth(text:str) -> bool:
    '''
    Takes in a string and returns True if the string is a month name
    '''
    text = text.upper().strip()
    for monthName in monthsofYear: #iteratrs thru months (not abbreviated)
        if text in monthName: #should account for even when month is abbreviated
            return True
    return False

def isDay(text:str) -> bool:
    '''
    Takes in a string and returns True if the string is a day of the week
    '''
    text = text.upper().strip()
    for dayName in daysOfTheWeekAsStrs: #iterates thru days of the week (not abbreviated)
        if text in dayName: #should account for even when day is abbreviated
            return True
    return False

def identifyDate(text:str, model: spacy.Language) -> dict:
    '''
    Takes a string and extracts all date information from the string. This function assumes that the given string contains a date with at least a day of the week or a day of a month. If no other date information is given, the function will fill out the rest of the dictionary values with the current date information.
    '''
    doc = model(text)
    dateInfo = []

    #extracting only the relevant date related info from the text
    dateInfo = getDocDateEnts(doc, dateInfo)
    
    #now that dateInfo has all the relevant date information, we need to reformat it into the dictionary
    dateDict = {}
    for aDate in dateInfo: #iterates by dates as lists of [dateStr, shapeStr]
        if aDate[0][0].isdigit(): #for dateStrs formatted as digits
            monthDigits = ""
            idx = 0
            while aDate[0][idx] != "/": #iterate by chars in dateStr
                monthDigits += aDate[0][idx]
                idx+=1
            monthDigits = int(monthDigits)
            if monthDigits > 12 or monthDigits < 1:
                monthDigits = (date.today()).month #gets current month from datetime if given month is invalid
            dateDict['month'] = [monthDigits]
            dateDict['month'] += months[monthDigits] #adds the month names in str form to the value list
            daysDigits = ""
            firstSlash = (aDate[0]).find('/') #can assume that dates formatted as digits will at least have mm/dd form
            for idx2 in range(firstSlash+1, len(aDate[0])):
                if aDate[0][idx2] != "/": #prevent from going into year part of the date
                    daysDigits += aDate[0][idx2]
                else:
                    secondSlash = idx2
            daysDigits = int(daysDigits)
            if daysDigits > 31 or daysDigits < 1:
                daysDigits = (date.today()).day #gets current day from datetime if given day is invalid (doesn't account for months with less than 31 days)
            dateDict['day'] = [daysDigits]
            if aDate[0].count('/') < 1: #then we know the date is formatted as MM/DD/YYYY
                yearDigits = ""
                for idx in range(secondSlash+1, len(aDate[0])):
                    yearDigits += aDate[0][idx]
                yearDigits = int(yearDigits)
                dateDict['year'] = [yearDigits]
            else: #then we know the date is formatted as MM/DD, we will assume they mean the current year
                dateDict['year'] = [(date.today()).year] #gets current year from 
        else: #for dates formatted as words
            print(aDate[0])
            aDate[0] = aDate[0].upper().strip().split() #capitalizes the date string
            if len(aDate[0]) > 1:
                aDate[0][0] = removeNonAlpha(aDate[0][0])
                aDate[0][1] = removeNonDigits(aDate[0][1])
                if len(aDate[0]) == 2: #if no year is provided, we assume this year
                    dateDict['year'] = [(date.today()).year]
                monthInt = findMonth(aDate[0][0])
                dateDict['month'] = [monthInt] + months[monthInt]
                dateDict['day'] = [int(aDate[0][1])]
            else: #if only one word is given, we assume it's a day of the week
                aDate[0] = aDate[0].upper().strip()
                #TODO: need to handle when only a day of the week is given
    #TODO: just realized this doesn't account for if a full date is provided like "Thursday, November 30th, 2023"

    # print(dateDict['month'])
    # print(dateDict['day'])
    # print(dateDict['year'])
    print(dateDict)

def getDocDateEnts(doc, dateInfo): 
    '''
    Gets spacy doc entities, specifically DATE entities, and adds them to the dateInfo list
    '''
    for ent in doc.ents:
        if ent.label_ == "DATE":
            dateStr = "" #for storing dates formatted as words because they get separated as tokens
            shapeStr = "" #for storing the shape of the token for dates formatted as words
            for token in doc:    
                if token.text == ent.text: #only works for dates formatted as digits
                    dateInfo.append([token.text, token.shape_])
                elif token.text in ent.text: #for when dates are formatted as words like day and month
                    dateStr += token.text + " "
                    shapeStr += token.shape_ + " "
                if token.text not in ent.text and dateStr != "": #then we know we've reached the end of the date
                    dateItem = [dateStr.strip(), shapeStr.strip()] 
                    if dateItem not in dateInfo: #prevents duplicates
                        dateInfo.append(dateItem)
    return dateInfo

def findMonth(date:str) -> int:
    '''
    Takes in a string and returns the month as an int
    '''
    month = 0
    for monthName in monthsofYear:
        if date in monthName:
            month = monthsofYear.index(monthName) + 1
    if month == 0: #in case given month is invalid
        month = (date.today()).month
    return month

def removeNonDigits(date: str) -> str:
    if date.isdigit():
        return date
    onlyDigits = False
    while not onlyDigits:
        for char in date:
            if not char.isdigit():
                date = date.replace(char, "")
        onlyDigits = True
    return date


def removeNonAlpha(date: str) -> str:
    if date.isalpha():
        return date
    onlyLetters = False
    while not onlyLetters:
        for char in date:
            if not char.isalpha():
                date = date.replace(char, "")
        onlyLetters = True
    return date
    
def createDate(dateString="") -> list:
    '''
    Takes in a string and returns a date as a list formatted as [month, day, year]
    dateStrings should have been parsed out of the original user input by spacy and identified as a DATE entity
    '''
    dateList = []
    if dateString == "":
        today = date.today()
        dateList[0] = int(today.strftime('%d'))
        dateList[1] = int(today.strftime('%m'))
        dateList[2] = int(today.strftime('%Y'))
    else: #TODO: need to handle when dateString is not empty and has different formats
        dateStringAsList = dateString.split() #make the dateString a list
        # check if spacy can identify dates formatted as MM/DD/YYYY （it does)
    

    return dateList

def extractApptData(text: str, model: spacy.Language) -> dict:
    '''
    Extracts appointment data from text and organizes it into a dictionary with the following appointment data:
    - date
    - time (optional)
    - location (optional)
    - reason
    '''
    apptData = {}
    doc = model(text)
    #get all the entities first that dates and times
    dates = []
    apptData['time'] = "" #empty value for in case a time isn't included
    for ent in doc.ents:
        if ent.label_ == "TIME":
            apptData['time'] = ent #need to make sure this value is saved as a str and not just some spacy entity
        if ent.label_ == "DATE":
            dates.append(ent)

    #TODO: need to separate months from days and handle different formatting
    
    return apptData

def extractWeatherData(text: str, model: spacy.Language) -> list:
    ''' 
    Extracts weather data from text and returns it as a list where the first element is the town/city, the second element is the state, and the third element is the country (optional)
    '''

    weatherData = []
    doc = model(text)
    entities = []

    #get all the entities first that are GPE (locations)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            entities.append(ent.text)
    
    #TODO: need to validate the locations are 1) real, 2), if the location is a state or city, 

def main():
    nlp = spacy.load("en_core_web_trf") #loads the pretrained model
    # identifyDate("I have an appointment on Nov. 30th at 3:00pm", nlp) #works
    # identifyDate("I have an appointment on 11/30 at 3:00pm", nlp) #works
    identifyDate("I have an appointment on Thursday at 3:00pm", nlp)

main()
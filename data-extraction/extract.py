import spacy
from datetime import date

nlp = spacy.load("en_core_web_trf") #loads the pretrained model

def identifyDate(text:str, model: spacy.Language) -> dict:
    '''
    Takes a string and extracts all date information from the string. This function assumes that the given string contains a date with at least a day of the week or a day of a month. If no other date information is given, the function will fill out the rest of the dictionary values with the current date information.
    '''
    doc = model(text)
    dateInfo = []
    
    #extracting only the relevant date related info from the text
    for ent in doc.ents:
        if ent.label_ == "DATE":
            for token in doc:
                dateStr = "" #for storing dates formatted as words because they get separated as tokens
                shapeStr = "" #for storing the shape of the token for dates formatted as words
                if token.text == ent.text: #only works for dates formatted as digits
                    dateInfo.append([token.text, token.shape_])
                elif token.text in ent.text: #for when dates are formatted as words like day and month
                    dateStr += token.text + " "
                    shapeStr += token.shape_ + " "
                if token.text not in ent.text and dateStr != "":
                    dateInfo.append([dateStr.strip(), shapeStr.strip()])
    
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


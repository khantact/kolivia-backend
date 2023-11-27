import spacy
from datetime import date

nlp = spacy.load("en_core_web_trf") #loads the pretrained model

def createDate(dateString="") -> list:
    '''
    Takes in a string and returns a date as a list formatted as [month, day, year]
    '''
    dateList = []
    if dateString == "":
        today = date.today()
        dateList[0] = int(today.strftime('%d'))
        dateList[1] = int(today.strftime('%m'))
        dateList[2] = int(today.strftime('%Y'))
    else: #TODO: need to handle when dateString is not empty and has different formats
        pass
    return dateList

def extractApptData(text: str, model: spacy.Language) -> dict:
    '''
    Extracts appointment data from text and organizes it into a dictionary with the following appointment data:
    - date
    - time
    - location
    - reason
    '''
    apptData = {}
    doc = model(text)

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


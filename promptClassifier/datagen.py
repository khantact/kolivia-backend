import glob
import random

actions = [
    "get a haircut",
    "attend a yoga class",
    "meet with a client",
    "visit the dentist",
    "have a date night",
    "schedule a doctor's appointment",
    "watch a movie with friends",
    "attend a parent-teacher conference",
    "go for a jog",
    "call a family meeting",
    "buy groceries",
    "pick up dry cleaning",
    "attend a job interview",
    "have a business meeting",
    "meet with a personal trainer",
    "go to a concert",
    "volunteer at a local charity",
    "take the dog for a walk",
    "have a spa day",
    "meet with a financial advisor",
    "go on a shopping spree",
    "plan a weekend getaway",
    "meet for a coffee date",
    "attend a workshop",
    "go to a tech conference",
    "plan a surprise party",
    "visit a museum",
    "set up a playdate for the kids",
    "attend a networking event",
    "join a support group",
    "host a dinner party",
    "have a therapy session",
    "attend a cooking class",
    "go on a hiking trip",
    "meet with a real estate agent",
    "attend a book club meeting",
    "take a scenic drive",
    "have a romantic dinner",
    "visit an art gallery",
    "plan a beach day",
    "meet with a travel agent",
    "go to a poetry reading",
    "have a picnic in the park",
    "attend a language class",
    "take a dance lesson",
    "meet with a nutritionist",
    "go on a museum tour",
    "plan a family reunion",
    "enjoy a spa massage",
    "meet with a life coach",
    "attend a cooking competition",
    "take a scenic bike ride",
    "go to a themed party",
    "host a barbecue cookout",
    "plan a romantic getaway",
    "have a picnic in the countryside",
    "meet with a career counselor",
    "participate in a charity run",
    "go to a local farmers' market",
    "attend a pet adoption event",
    "have a game night with friends",
    "plan a visit to a botanical garden",
    "enjoy a scenic train ride",
    "meet with a travel blogger",
    "go to a local art exhibition",
    "attend a stand-up comedy show",
    "have a family movie night",
    "visit a historical landmark",
    "plan a visit to an amusement park",
    "go to a karaoke night",
    "host a potluck dinner",
    "attend a wine tasting event",
    "take a nature hike",
    "meet with a personal stylist",
    "go to a craft fair",
    "plan a visit to an aquarium",
    "have a game of mini-golf",
    "visit a wildlife sanctuary",
    "attend a poetry slam",
    "go to a car show",
    "host a themed costume party",
    "plan a day at the beach",
    "meet with a tattoo artist",
    "go to a themed escape room",
    "attend a lecture on art history",
    "have a science experiment day",
    "visit a botanical garden",
    "plan a visit to a space museum",
    "go to a trampoline park",
    "host a talent show",
    "attend a food festival",
    "take a painting class",
    "meet with a life coach",
    "go to a dance competition",
    "plan a visit to a planetarium",
    "have a karaoke night with friends",
    "visit a wildlife reserve",
    "attend a local theater performance",
    "go to a storytelling event",
    "host a board game night",
    "plan a visit to a science center",
    "meet with a nutritionist",
    "go to a classic car show",
    "have a spa day with friends",
    "visit an outdoor art exhibit",
    "attend a jazz music concert",
    "go to a cooking workshop",
    "host a barbecue party",
    "plan a visit to a tropical garden",
    "meet with a wellness coach",
    "go to a petting zoo",
    "have a photography workshop",
    "visit a children's science museum",
    "attend a live theater performance",
    "go to a dance recital",
    "host a craft night with friends",
    "plan a visit to a botanical conservatory",
    "meet with a financial advisor",
    "go to a stand-up comedy club",
    "have a tea tasting with friends",
    "visit an interactive science museum",
    "attend a photography exhibit",
    "go to a wine and paint night",
    "host a themed trivia night",
    "plan a visit to a butterfly garden",
    "meet with a pet trainer",
    "go to a documentary screening",
    "have a puzzle-solving competition",
    "visit a marine life sanctuary",
    "attend a live music festival",
    "go to a DIY crafting workshop",
    "host a themed costume party",
    "plan a visit to a historic mansion",
    "meet with a life coach",
    "go to a board game cafe",
    "have a themed movie night with friends",
    "visit a wildlife rehabilitation center",
    "attend a circus performance",
    "go to a pottery painting class",
    "host a charity fundraising event",
    "plan a visit to a planetarium",
    "meet with a tarot card reader",
    "go to a comedy improv show",
    "have a sushi-making night with friends",
    "visit a local food truck festival",
    "attend a vintage car show",
    "go to a photography scavenger hunt",
    "host a scavenger hunt",
    "plan a visit to a hot air balloon festival",
    "meet with a personal trainer",
    "go to a food and wine pairing event",
    "have a cupcake decorating competition",
    "visit a reptile sanctuary",
    "attend a magic show",
    "go to a classic film screening",
    "host a themed costume party",
    "plan a visit to a historic castle",
    "meet with a relationship counselor",
    "go to a stand-up comedy club",
    "have a themed cooking competition with friends",
    "visit a botanical garden",
    "attend a garden party",
    "go to a wine and cheese tasting event",
    "host a themed game night",
    "plan a visit to a butterfly conservatory",
    "meet with a personal coach",
    "go to a bird-watching expedition",
    "have a puzzle-solving challenge with friends",
    "visit a wildlife rescue center",
    "attend a live jazz music performance",
    "go to a photography exhibition",
    "host a pottery painting night",
    "plan a visit to a historic lighthouse",
    "meet with a yoga instructor",
    "go to a comedy club",
    "have a themed movie marathon",
    "visit a local food and wine festival",
    "attend a vintage clothing expo",
    "go to a photography workshop",
    "host a charity auction event",
    "plan a visit to an observatory",
    "meet with a palm reader",
    "go to an improv theater show",
    "have a chocolate-tasting night with friends",
    "visit a chocolate factory tour",
    "attend a classic car exhibit",
    "go to a DIY home improvement workshop",
    "host a board game night with friends",
    "plan a visit to a historical village",
    "meet with a career counselor",
    "go to a local theater play",
    "have a themed costume party with friends",
    "visit a tropical bird sanctuary",
    "attend a live stand-up comedy show",
    "go to a wine and painting night",
    "host a themed trivia game night",
    "plan a visit to a botanical rainforest",
    "meet with a wellness coach",
    "go to a pet adoption event",
    "have a craft beer tasting with friends",
    "visit an art and wine gallery",
    "attend a photography class",
    "go to a cooking competition",
    "host a potluck dinner",
    "plan a visit to a historical reenactment",
    "meet with a personal trainer",
    "go to a dance competition",
    "have a karaoke night with friends",
    "visit a wildlife reserve",
    "attend a local theater performance",
    "go to a storytelling event",
    "host a board game night",
    "plan a visit to a science center",
    "meet with a nutritionist",
    "go to a classic car show",
    "have a spa day with friends",
    "visit an outdoor art exhibit",
    "attend a jazz music concert",
    "go to a cooking workshop",
    "host a barbecue party",
    "plan a visit to a tropical garden",
    "meet with a wellness coach",
    "go to a petting zoo",
    "have a photography workshop",
    "visit a children's science museum",
    "attend a live theater performance",
    "go to a dance recital",
    "host a craft night with friends",
    "plan a visit to a botanical conservatory",
    "meet with a financial advisor",
    "go to a stand-up comedy club",
    "have a tea tasting with friends",
    "visit an interactive science museum",
    "attend a photography exhibit",
    "go to a wine and paint night",
    "host a themed trivia night",
    "plan a visit to a butterfly garden",
    "meet with a pet trainer",
    "go to a documentary screening",
    "have a puzzle-solving competition",
    "visit a marine life sanctuary",
    "attend a live music festival",
    "go to a DIY crafting workshop",
    "host a themed costume party",
    "plan a visit to a historic mansion",
    "meet with a life coach",
    "go to a board game cafe",
    "have a themed movie night with friends",
    "visit a wildlife rehabilitation center",
    "attend a circus performance",
    "go to a pottery painting class",
    "host a charity fundraising event",
    "plan a visit to a planetarium",
    "meet with a tarot card reader",
    "go to a comedy improv show",
    "have a sushi-making night with friends",
    "visit a local food truck festival",
    "attend a vintage car show",
    "go to a photography scavenger hunt",
    "host a scavenger hunt",
    "plan a visit to a hot air balloon festival",
    "meet with a personal trainer",
    "go to a food and wine pairing event",
    "have a cupcake decorating competition",
    "visit a reptile sanctuary",
    "attend a magic show",
    "go to a classic film screening",
    "host a themed costume party",
    "plan a visit to a historic castle",
    "meet with a relationship counselor",
    "go to a stand-up comedy club",
    "have a themed cooking competition with friends",
    "visit a botanical garden",
    "attend a garden party",
    "go to a wine and cheese tasting event",
    "host a themed game night",
    "plan a visit to a butterfly conservatory",
    "meet with a personal coach",
    "go to a bird-watching expedition",
    "have a puzzle-solving challenge with friends",
    "visit a wildlife rescue center",
    "attend a live jazz music performance",
    "go to a photography exhibition",
    "host a pottery painting night",
    "plan a visit to a historic lighthouse",
    "meet with a yoga instructor",
    "go to a comedy club",
    "have a themed movie marathon",
    "visit a local food and wine festival",
    "attend a vintage clothing expo",
    "go to a photography workshop",
    "host a charity auction event",
    "plan a visit to an observatory",
    "meet with a palm reader",
    "go to an improv theater show",
    "have a chocolate-tasting night with friends",
    "visit a chocolate factory tour",
    "attend a classic car exhibit",
    "go to a DIY home improvement workshop",
    "host a board game night with friends",
    "plan a visit to a historical village",
]
eval_actions = [
    "take a pottery class",
    "go on a wine tour",
    "visit a botanical park",
    "plan a day at the zoo",
    "meet with a personal chef",
    "attend a science fair",
    "have a movie marathon",
    "go on a road trip",
    "host a themed costume party",
    "schedule a spa day",
    "meet for a coffee date",
    "visit an escape room",
    "plan a visit to an art museum",
    "have a picnic by the lake",
    "go to a farmers' market",
    "watch a live theater performance",
    "organize a charity run",
    "meet with a life coach",
    "go on a photography expedition",
    "host a board game night",
    "attend a poetry reading",
    "take a scenic helicopter ride",
    "visit a wildlife sanctuary",
    "plan a visit to a botanical conservatory",
    "meet with a financial advisor",
    "go to a stand-up comedy show",
    "have a tea tasting with friends",
    "go on a museum tour",
    "attend a cooking competition",
    "take a scenic bike ride",
    "visit an outdoor art exhibit",
    "host a barbecue cookout",
    "plan a romantic getaway",
    "have a picnic in the countryside",
    "meet with a career counselor",
    "participate in a charity walk",
    "go to a local art exhibition",
    "attend a live music festival",
    "watch a live sports game",
    "organize a treasure hunt",
    "host a craft night with friends",
    "schedule a wine and cheese tasting",
    "meet for a game night",
    "go on a hot air balloon ride",
    "visit a historical castle",
    "plan a visit to a space museum",
    "have a spa day with friends",
    "meet with a travel blogger",
    "go to a petting zoo",
    "attend a children's science museum",
    "take a dance lesson",
    "host a themed trivia night",
    "plan a visit to a butterfly garden",
    "meet with a pet trainer",
    "go on a documentary screening",
    "have a puzzle-solving competition",
    "visit a marine life sanctuary",
    "attend a vintage car show",
    "go on a shopping spree",
    "plan a visit to a historic mansion",
    "meet with a life coach",
    "go to a board game cafe",
    "have a themed movie night with friends",
    "attend a circus performance",
    "watch a live magic show",
    "organize a painting workshop",
    "host a charity fundraising event",
    "schedule a visit to an observatory",
    "meet with a palm reader",
    "go on an improv theater show",
    "have a sushi-making night with friends",
    "visit a local food truck festival",
    "take a cooking class",
    "plan a visit to an aquarium",
    "attend a stand-up comedy club",
    "meet for a game of mini-golf",
    "go on a wildlife safari",
    "host a karaoke night",
    "schedule a nature hike",
    "visit an art and wine gallery",
    "have a cupcake decorating competition",
    "meet with a personal stylist",
    "go on a historic train ride",
    "plan a visit to a tropical garden",
    "attend a wine tasting event",
    "watch a live jazz music concert",
    "organize a scavenger hunt",
    "host a themed costume party with friends",
    "take a scenic cruise",
    "go to a bird-watching expedition",
    "meet with a wellness coach",
    "visit an indoor trampoline park",
    "have a puzzle-solving challenge with friends",
    "attend a local theater play",
    "go on a pottery painting class",
    "plan a visit to a wildlife rehabilitation center",
    "meet with a travel agent",
    "schedule a visit to a planetarium",
    "organize a night of comedy improv",
    "host a chocolate-tasting night with friends",
    "take a trip to a chocolate factory",
    "meet for a classic film screening",
    "go on a DIY home improvement workshop",
    "visit an interactive science museum",
    "have a family game night",
    "plan a visit to a butterfly conservatory",
    "attend a photography class",
    "watch a wine and paint night",
    "meet with a personal coach",
    "go on a pet adoption event",
    "schedule a themed cooking competition",
    "visit an exotic botanical garden",
    "organize a garden party",
    "have a movie marathon with friends",
    "meet for a wine and cheese tasting event",
    "go on a hike to a scenic waterfall",
    "host a board game night with friends",
    "take a scenic hot air balloon ride",
    "attend a vintage clothing expo",
    "go on a photography workshop",
    "plan a visit to a wildlife rescue center",
    "meet with a relationship counselor",
    "organize a themed trivia night",
    "host a game night with friends",
    "schedule a visit to a historic lighthouse",
    "go on a visit to a yoga retreat",
    "meet with a yoga instructor",
    "have a tea tasting party with friends",
    "visit a classic car exhibit",
    "attend a local theater performance",
    "watch a live music festival",
    "plan a visit to a comedy club",
    "go on a pottery painting night",
    "organize a dance competition",
    "host a stand-up comedy show",
    "take a scenic horseback ride",
    "meet for a craft night with friends",
    "schedule a visit to a botanical rainforest",
    "visit an outdoor art exhibit",
    "have a barbecue party with friends",
    "go on a visit to a tropical garden",
    "meet with a wellness coach",
    "plan a visit to a petting zoo",
    "attend a documentary screening",
    "organize a craft beer tasting night",
    "watch a themed costume party",
    "host a spa day with friends",
    "take a scenic boat tour",
    "meet for a karaoke night",
    "schedule a wildlife safari",
    "visit a wildlife reserve",
    "plan a visit to a children's science museum",
    "attend a live theater performance",
    "go on a dance recital",
    "organize a classic film screening",
    "host a craft night with friends",
    "watch a live jazz music concert",
    "take a visit to an art gallery",
    "meet with a nutritionist",
    "schedule a cooking workshop",
    "visit a science center",
    "have a themed costume party",
    "organize a board game night",
    "go on a visit to a classic car show",
    "meet with a pet trainer",
    "watch a themed trivia night",
    "host a spa day with friends",
    "take a pottery class",
    "visit a botanical park",
    "plan a day at the zoo",
    "meet with a personal chef",
    "attend a science fair",
    "have a movie marathon",
    "go on a road trip",
    "host a themed costume party",
    "schedule a spa day",
    "meet for a coffee date",
    "visit an escape room",
    "plan a visit to an art museum",
    "have a picnic by the lake",
    "go to a farmers' market",
    "watch a live theater performance",
    "organize a charity run",
    "meet with a life coach",
    "go on a photography expedition",
    "host a board game night",
    "attend a poetry reading",
    "take a scenic helicopter ride",
    "visit a wildlife sanctuary",
    "plan a visit to a botanical conservatory",
    "meet with a financial advisor",
    "go to a stand-up comedy show",
    "have a tea tasting with friends",
    "go on a museum tour",
    "attend a cooking competition",
    "take a scenic bike ride",
    "visit an outdoor art exhibit",
    "host a barbecue cookout",
    "plan a romantic getaway",
    "have a picnic in the countryside",
    "meet with a career counselor",
    "participate in a charity walk",
    "go to a local art exhibition",
    "attend a live music festival",
    "watch a live sports game",
    "organize a treasure hunt",
    "host a craft night with friends",
    "schedule a wine and cheese tasting",
    "meet for a game night",
    "go on a hot air balloon ride",
    "visit a historical castle",
    "plan a visit to a space museum",
    "have a spa day with friends",
    "meet with a travel blogger",
    "go to a petting zoo",
    "attend a children's science museum",
    "take a dance lesson",
    "host a themed trivia night",
    "plan a visit to a butterfly garden",
    "meet with a pet trainer",
    "go on a documentary screening",
    "have a puzzle-solving competition",
    "visit a marine life sanctuary",
    "attend a vintage car show",
    "go on a shopping spree",
    "plan a visit to a historic mansion",
    "meet with a life coach",
    "go to a board game cafe",
    "have a themed movie night with friends",
    "attend a circus performance",
    "watch a live magic show",
    "organize a painting workshop",
    "host a charity fundraising event",
    "schedule a visit to an observatory",
    "meet with a palm reader",
    "go on an improv theater show",
    "have a chocolate-tasting night with friends",
    "visit a chocolate factory tour",
    "attend a classic car exhibit",
    "go to a DIY home improvement workshop",
    "host a board game night with friends",
    "plan a visit to a historical village",
]
small_actions = [
    "plan a hiking trip",
    "have a picnic in the mountains",
    "go on a camping adventure",
    "attend a wine and cheese tasting event",
    "take a photography workshop",
    "organize a beach cleanup",
    "visit an archaeological site",
    "host a themed costume party",
    "plan a visit to a historic lighthouse",
    "have a spa day with friends",
    "meet with a wellness coach",
    "attend a local food and wine festival",
    "go on a photography workshop",
    "organize a charity auction event",
    "visit an observatory",
    "have a movie night under the stars",
    "plan a visit to a botanical rainforest",
    "meet with a yoga instructor",
    "attend a vintage clothing expo",
    "go on a pottery painting class",
    "host a craft beer tasting with friends",
    "take a scenic boat tour",
    "visit a wildlife reserve",
    "organize a board game night",
    "plan a visit to a classic car show",
    "have a themed trivia night",
    "meet with a pet trainer",
    "go on a pottery class",
    "take a wine tour",
    "visit a botanical park",
    "plan a day at the zoo",
    "meet with a personal chef",
    "attend a science fair",
    "go on a road trip",
    "schedule a spa day",
    "plan a visit to an art museum",
    "have a picnic by the lake",
    "go to a farmers' market",
    "watch a live theater performance",
    "organize a charity run",
    "meet with a life coach",
    "go on a photography expedition",
    "host a board game night",
    "attend a poetry reading",
    "take a scenic helicopter ride",
    "plan a visit to a botanical conservatory",
    "meet with a financial advisor",
    "go to a stand-up comedy show",
    "have a tea tasting with friends",
    "go on a museum tour",
    "attend a cooking competition",
    "take a scenic bike ride",
    "visit an outdoor art exhibit",
    "host a barbecue cookout",
    "plan a romantic getaway",
    "have a picnic in the countryside",
    "meet with a career counselor",
    "participate in a charity walk",
    "go to a local art exhibition",
    "attend a live music festival",
    "watch a live sports game",
    "organize a treasure hunt",
    "host a craft night with friends",
    "schedule a wine and cheese tasting",
    "meet for a game night",
    "go on a hot air balloon ride",
    "visit a historical castle",
    "plan a visit to a space museum",
    "have a spa day with friends",
    "meet with a travel blogger",
    "go to a petting zoo",
    "attend a children's science museum",
    "take a dance lesson",
    "host a themed trivia night",
    "plan a visit to a butterfly garden",
    "meet with a pet trainer",
    "go on a documentary screening",
    "have a puzzle-solving competition",
    "visit a marine life sanctuary",
    "attend a vintage car show",
    "go on a shopping spree",
    "plan a visit to a historic mansion",
    "meet with a life coach",
    "go to a board game cafe",
    "have a themed movie night with friends",
    "attend a circus performance",
    "watch a live magic show",
    "organize a painting workshop",
    "host a charity fundraising event",
    "schedule a visit to an observatory",
    "meet with a palm reader",
    "go on an improv theater show",
    "have a chocolate-tasting night with friends",
    "visit a chocolate factory tour",
    "attend a classic car exhibit",
    "go to a DIY home improvement workshop",
    "host a board game night with friends",
    "plan a visit to a historical village",
    "go on a visit to a yoga retreat",
    "meet with a yoga instructor",
    "have a tea tasting party with friends",
    "visit a classic car exhibit",
]


def generateDates() -> dict:
    """
    generates a dictionary dates with keys 'days' and 'months'
    each key maps to another dictionary specifically for storing different representations of the days and months as full words, 3 letter abbreviations, and numbers (still in str)

    preview: (changed everything in lowercase for easier identification)
        dates = {'days': {'daysOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'days3LetVer': ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'], 'daysAbbrev': ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']}, 'months': {'months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 'months3LetVer': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], 'monthNums': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']}}
    """
    dates = {}
    daysOfWeek = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    days3LetVer = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    # daysAbbrev = ["m", "t", "w", "th", "f", "sa", "su"]
    # daysDict = {"daysOfWeek": daysOfWeek, "days3LetVer": days3LetVer, "daysAbbrev": daysAbbrev}
    daysDict = {"daysOfWeek": daysOfWeek, "days3LetVer": days3LetVer}
    dates["days"] = daysDict

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    months3LetVer = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    monthNums = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ]  # can all be converted to ints
    monthsDict = {
        "months": months,
        "months3LetVer": months3LetVer,
        "monthNums": monthNums,
    }
    dates["months"] = monthsDict

    return dates


def generateDatePhrase(dates: dict) -> str:
    """
    for generating date phrases such as
    - "on {dayOfTheWeek}" -- (e.g, "on Monday")
    - "on {dayOfTheWeek}, {month} {date}" -- (e.g., "on Monday, January 1st")
    - "on {month} {date}" -- (e.g., "on January 1st")
    - "on the {date} of {month} -- (e.g., "on the 1st of January")
    - "on {dayOfTheWeek} the {date} of {month} -- (e.g., "on Monday the 1st of January")

    - "for {dayOfTheWeek}" -- (e.g., "for Monday")
    - "for {month} {date}" -- (e.g., "for January 1st")
    - "for" {dayOfTheWeek}, {month} {date}" -- (e.g., "for Monday, January 1st")
    - "for this {dayOfTheWeek}" -- (e.g., "for this Monday")
    - "for next {dayOfTheWeek}" -- (e.g., "for next Monday")

    """
    monthDictKey = random.choice(
        ["months", "months3LetVer", "monthNums"]
    )  # randomly choose month format
    month = random.choice(
        dates["months"][monthDictKey]
    )  # randomly choose month in chosen format
    if month.isdigit():  # if month is in number format
        month = str(
            int(month)
        )  # convert to int and then back to str to remove leading 0
    # dayDictKey = random.choice(['daysOfWeek', 'days3LetVer', 'daysAbbrev']) #randomly chose day format
    dayDictKey = random.choice(
        ["daysOfWeek", "days3LetVer"]
    )  # randomly chose day format
    day = random.choice(
        dates["days"][dayDictKey]
    )  # randomyl choose day of the week in chosen format

    # need to outline conditionals for constructing valid date
    have31Days = [
        "january",
        "march",
        "may",
        "july",
        "august",
        "october",
        "december",
        "01",
        "03",
        "05",
        "07",
        "08",
        "10",
        "12",
        "jan",
        "mar",
        "may",
        "jul",
        "aug",
        "oct",
        "dec",
    ]
    have30Days = [
        "april",
        "june",
        "september",
        "november",
        "04",
        "06",
        "09",
        "11",
        "apr",
        "jun",
        "sept",
        "nov",
    ]
    date = 0
    # print(month)
    if month in have31Days:
        date = random.randint(1, 31)
    elif month in have30Days:
        date = random.randint(1, 30)
    else:
        date = random.randint(1, 28)

    # need to reformat str of date to include "st", "nd", "rd", or "th" at the end
    if month.isdigit() == False:  # if month is in number format
        if date > 3 and date < 21:
            date = str(date) + "th"
        else:
            remainder = date % 10
            if remainder == 1:
                date = str(date) + "st"
            elif remainder == 2:
                date = str(date) + "nd"
            elif remainder == 3:
                date = str(date) + "rd"
            else:
                date = str(date) + "th"

    # randomly choose a phrase format
    """
    - "on {dayOfTheWeek}, {month} {date}" -- (e.g., "on Monday, January 1st")
    - "on {month} {date}" -- (e.g., "on January 1st")
    """
    phrases = [
        f"on {day}",
        f"on {day}, {month} {date}"
        if month.isdigit() == False
        else f"on {day}, {month}/{date}",
        f"on {month}/{date}"
        if month.isdigit()
        else f"on {month} {date}",  # inline ifs reformat the str if months are also in number format
        f"on the {date} of {month}"
        if month.isdigit() == False
        else f"on the {date} of {dates['months'][random.choice(['months', 'months3LetVer'])][int(month)-1]}",
        f"on {day} the {date} of {month}"
        if month.isdigit() == False
        else f"on {day} the {date} of {dates['months'][random.choice(['months', 'months3LetVer'])][int(month)-1]}",
        f"for {day}",
        f"for this {day}",
        f"for next {day}",
        f"for {month}/{date}" if month.isdigit() else f"for {month} the {date}",
        f"for {day}, {month}/{date}"
        if month.isdigit()
        else f"for {day}, {month} {date}",
    ]
    return random.choice(phrases)


def generateWeatherPhrasePrompt(dataSet: int):
    """
    generates a weather phrase prompt such as
    - "what's the weather like today?"
    - "what's the weather like tomorrow?"
    - "what's the weather like on {dayOfTheWeek}?"
    - "what's the weather like on {month} {date}?"
    - "what's the weather like on {dayOfTheWeek}, {month} {date}?"
    - "what's the weather like for {dayOfTheWeek}?"
    - "what's the weather like for {month} {date}?"
    - "what's the weather like for {dayOfTheWeek}, {month} {date}?"
    - "what's the weather like for this {dayOfTheWeek}?"
    - "what's the weather like for next {dayOfTheWeek}?"
    - "what's the weather like for {month}/{date}?"
    - "what's the weather like for {dayOfTheWeek}, {month}/{date}?"
    """
    dates = generateDates()
    datePhrase = generateDatePhrase(dates)
    weatherPhrase1 = [
        "what's the weather like today?",
        "Can you tell me about today's weather?",
        "How's the weather looking right now?",
        "Is it going to rain today?",
        "What's the forecast for today?",
        "Could you give me an update on today's weather?",
        "What should I expect from the weather today?",
        "Any idea about today's weather conditions?",
        "How's the climate shaping up for today?",
        "Will it be sunny or cloudy today?",
        "Do you have information on today's weather patterns?",
        "Can you inform me about the atmospheric conditions today?",
        "What's the outlook for the weather today?",
        "Any news on today's weather forecast?",
        "Could you let me know what the sky looks like today?",
        "Is there any precipitation expected today?",
        "Can you provide details on today's weather report?",
        "How's the temperature today?",
        "What's the weather situation for today?",
        "Will there be any storms today?",
        "Can you share the weather updates for today?",
        "Do you have the latest on today's weather forecast?",
        "Is there a chance of snow or rain today?",
        "How's the weather shaping up for today's plans?",
        "What's the atmospheric outlook for today?",
        "Could you check and let me know about today's weather?",
        "Any idea if it's going to be windy today?",
        "What does today's weather map show?",
        "Can you inform me about the current weather conditions today?",
        "How should I prepare for today's weather?",
        "Is it going to be a hot or cold day today?",
        "What can you tell me about the weather today?",
        "Any updates on today's weather situation?",
        "How's the weather forecast for today looking?",
        "What's the temperature range for today?",
        "Will there be any weather-related disruptions today?",
        "Can you provide a summary of today's weather outlook?",
        "What's the word on today's weather?",
        "Is there any chance of fog or mist today?",
        "Could you give me a heads up on what to expect weather-wise today?"
        f"what's the weather like tomorrow?",
        f"what's the weather like {datePhrase}?",
        f"what's the weather like for {datePhrase}?",
    ]
    weatherPhrase2 = [
        "What's the weather like right now?",
        "Any updates on the current weather conditions?",
        "Can you give me a real-time weather report?",
        "Is there any precipitation in the forecast?",
        "How's the temperature at this moment?",
        "What's the immediate weather outlook?",
        "Could you describe the current atmospheric conditions?",
        "Is there any chance of rain or snow in the next hour?",
        "Can you provide a quick weather summary for the next few hours?",
        "How should I dress for the current weather?",
        "What's the ongoing weather situation?",
        "Any alerts or warnings for the current weather?",
        "What's the atmospheric pressure right now?",
        "Can you update me on the latest weather developments?",
        "How is the weather evolving at this instant?",
        "Is the wind speed significant at the moment?",
        "What's the visibility like right now?",
        "Can you share the current weather patterns?",
        "Is there any extreme weather expected shortly?",
        "How's the weather expected to change in the next hour?",
        f"what's the weather like tomorrow?",
        f"what's the weather like {datePhrase}?",
        f"what's the weather like for {datePhrase}?",
    ]
    weatherPhrase3 = [
        "What's the weather like for the upcoming weekend?",
        "Can you provide a forecast for the next seven days?",
        "Any insights into the weather for the rest of the week?",
        "How's the weather expected to change tomorrow?",
        "Could you give me an overview of the weather in the coming days?",
        "What's the long-term weather outlook?",
        "Any special weather considerations for the next few days?",
        "How's the weather shaping up for the weekend?",
        "Can you tell me about the weather conditions for the next month?",
        "What's the extended forecast like?",
        "Any significant weather events anticipated in the near future?",
        "How should I prepare for the weather in the coming weeks?",
        "Can you give me an idea of the weather trends in the upcoming month?",
        "What's the expected weather pattern for the next fortnight?",
        "Could you provide a summary of the weather over the next month?",
        "Any unusual weather phenomena expected in the next few weeks?",
        "How's the weather looking for outdoor activities next week?",
        "What's the general weather trend for the upcoming season?",
        "Can you give me a heads up on any weather anomalies expected soon?",
        "What's the weather forecast like for the next quarter?",
        f"what's the weather like tomorrow?",
        f"what's the weather like {datePhrase}?",
        f"what's the weather like for {datePhrase}?",
    ]
    if dataSet == 1:
        return random.choice(weatherPhrase1)
    elif dataSet == 2:
        return random.choice(weatherPhrase2)
    return random.choice(weatherPhrase3)


def popTimes():
    times = []
    for x in ["AM", "PM"]:
        for i in range(1, 13):
            for j in range(1, 60):
                if j < 10:
                    j = "0" + str(j)
                times.append(str(i) + ":" + str(j) + x)
    return times


# TODO: will need to add cases where prompts include durations of times
def createAppointmentPrompt(time, action, trainOrEval):
    appointment_formats = [
        f"Schedule an appointment to {action} at {time}",
        f"Set up a meeting at {time} to {action}",
        f"Plan an event for {time} involving {action}",
        f"Book a reservation at {time} to {action}",
        f"I'd like to have an appointment at {time} to {action}",
        f"Please pencil me in at {time} to {action}",
        f"Reserve a spot to {action} at {time}",
        f"Organize a session at {time} to {action}",
        f"Create an event to {action} on {time}",
        f"Block time in my schedule to {action} at {time}",
        f"Arrange a meeting at {time} to discuss {action}",
        f"Plan an appointment on {time} to {action}",
        f"Book a slot at {time} to {action}",
        f"Reschedule a commitment to {time} to {action}",
        f"Fix a meeting to {action} at {time}",
        f"Add an event to my calendar at {time} to {action}",
        f"Block time to {action} at {time}",
        f"Set a reminder to {action} at {time}",
        f"Arrange an appointment with me at {time} to {action}",
        f"Mark my calendar to {action} at {time}",
        f"I'd like to {action} at {time}",  # implicit command - siri responds to this
    ]
    eval_appoints = [
        f"Secure a timeslot for {action} at {time}",
        f"Plan a meeting with {action} at {time}",
        f"Coordinate an event for {action} at {time}",
        f"Book a reservation for {action} at {time}",
        f"Reserve a spot for {action} at {time}",
        f"Block out time for {action} on {time}",
        f"Set up a session with {action} at {time}",
        f"Schedule a gathering for {action} at {time}",
        f"Arrange a discussion at {time} regarding {action}",
        f"Create a calendar entry for {action} at {time}",
        f"Design an appointment for {action} at {time}",
        f"Plan a meeting to discuss {action} at {time}",
        f"Hold a reservation for {action} at {time}",
        f"Organize an event involving {action} at {time}",
        f"Fix a commitment for {action} at {time}",
        f"Mark my calendar for a meeting with {action} at {time}",
        f"Block off time for a session on {time} with {action}",
        f"Book an appointment to {action} at {time}",
        f"Schedule a reminder for {action} at {time}",
        f"Arrange a conference at {time} about {action}",
        f"I'm going to {action} at {time}",  # implicit command - siri responds to this
    ]
    different_appointment_formats = [
        f"Set up a meeting for {time} to {action}",
        f"Plan an appointment at {time} for {action}",
        f"Block time in my schedule on {time} for {action}",
        f"Create an event for {action} at {time}",
        f"Book a reservation at {time} for {action}",
        f"Reserve a spot at {time} for an appointment about {action}",
        f"Organize a session for {action} at {time}",
        f"Mark my calendar for a meeting at {time} to discuss {action}",
        f"Block out time on {time} for a commitment to {action}",
        f"Arrange an appointment at {time} to talk about {action}",
        f"Hold a reservation for an event related to {action} at {time}",
        f"Fix a meeting for {action} at {time}",
        f"Design an appointment involving {action} at {time}",
        f"Schedule a reminder for an appointment about {action} at {time}",
        f"Coordinate a gathering at {time} for {action}",
        f"Book a slot at {time} for an appointment concerning {action}",
        f"Secure a timeslot on {time} for a discussion about {action}",
        f"Create a calendar entry at {time} for an appointment related to {action}",
        f"Plan a meeting to {action} at {time}",
        f"Arrange a conference for {action} at {time}",
    ]
    datesDict = generateDates()
    datePhrase = generateDatePhrase(datesDict)
    addDatePhrase = random.choice(
        [True, False]
    )  # boolean for deciding when to add date phrase to appointment prompt
    chosenFormat = ""
    if trainOrEval == 0:
        chosenFormat = random.choice(eval_appoints)
    elif trainOrEval == 1:
        chosenFormat = random.choice(appointment_formats)
    else:
        chosenFormat = random.choice(different_appointment_formats)
    if addDatePhrase:  # add date phrase if boolean is true
        chosenFormat = chosenFormat + " " + datePhrase
    return chosenFormat


def populateSmallApptData():
    prompts = []
    times = popTimes()
    print("running...")
    for i in range(10000):
        time = random.choice(times)
        action = random.choice(small_actions)
        prompts.append(createAppointmentPrompt(time, action, 2))
    with open("data/train_data/appointments.txt", "w") as f:
        for prompt in prompts:
            f.write(prompt)
            f.write("\n")


def populateWeatherData(num: int, filePath: str, dataSet: int):
    prompts = []
    for i in range(num):
        prompts.append(generateWeatherPhrasePrompt(dataSet))
    with open(filePath, "w") as f:
        for prompt in prompts:
            f.write(prompt)
            f.write("\n")


def main():
    prompts = []
    evalPrompts = []
    times = popTimes()
    print("running...")
    for i in range(40000):
        time = random.choice(times)
        action = random.choice(actions)
        prompts.append(createAppointmentPrompt(time, action, 1))

    for i in range(40000):
        time = random.choice(times)
        action = random.choice(eval_actions)
        evalPrompts.append(createAppointmentPrompt(time, action, 0))

    with open("data/test_data/appointments.txt", "w") as f:
        for prompt in prompts:
            f.write(prompt)
            f.write("\n")

    with open("data/eval_data/appointments.txt", "w") as f:
        for prompt in evalPrompts:
            f.write(prompt)
            f.write("\n")


# main()
populateWeatherData(10000, "data/train_data/weather.txt", 1)
populateWeatherData(40000, "data/test_data/weather.txt", 2)
populateWeatherData(40000, "data/eval_data/weather.txt", 3)
populateSmallApptData()
# dates = generateDates()
# print(createAppointmentPrompt("12:00PM", "go to a pottery painting class", 1))

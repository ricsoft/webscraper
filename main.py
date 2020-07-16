from breweries.breweries import getYellowdog, getMoodyales, getParkside, getTwinsails
from db.dynamodb import addToDynamodb

# scrap beer from breweries
yellowdogList = getYellowdog()
moodyalesList = getMoodyales()
parksideList = getParkside()
twinsailsList = getTwinsails()

# upload beer to dynamodb
breweryList = [yellowdogList, moodyalesList, parksideList, twinsailsList]
res = addToDynamodb(breweryList)

print(res)
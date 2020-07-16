from breweries.breweries import getYellowdog, getMoodyales, getParkside, getTwinsails
from db.dynamodb import addToDynamodb

yellowdogList = getYellowdog()
moodyalesList = getMoodyales()
parksideList = getParkside()
twinsailsList = getTwinsails()

print(*yellowdogList)
print(*moodyalesList)
print(*parksideList)
print(*twinsailsList)


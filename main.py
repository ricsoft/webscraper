from breweries.breweries import *
from db.dynamodb import addToDynamodb

# scrap beer from breweries
# then upload beer to dynamodb
breweryList = [getDageraad(), getYellowdog(), getMoodyales(), getParkside(), getTwinsails(), getFrasermills()]
print(addToDynamodb(breweryList))


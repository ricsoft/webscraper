from breweries.helpers import getChromeDriver, fillBeerList, stripNewLine, spaceBeforeCapital

yellowdogUrl = 'https://yellowdogbeer.com/tasting-room'
moodyalesUrl = 'http://www.moodyales.com'
parksideUrl = 'http://www.theparksidebrewery.com/tasting-room'
twinsailsUrl = 'https://twinsailsbrewing.com/our-beers/'

def getYellowdog():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="untappd__beer-row__name"]'
        beerName = ['h3.untappd__beer-row__name']
        beerType = 'h5.untappd__beer-row__style'
        beerList = fillBeerList(driver, yellowdogUrl, waitFor, beerName, beerType)

    except:
        print('Error getYellowdog')

    driver.quit()

    return beerList

def getMoodyales():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="details"]'
        beerName = ['div.beers-ontap div.row div.col-md-12:nth-child(1) ul li a', 'div.beers-ontap div.row div.col-md-12:nth-child(1) ul li span']
        beerList = fillBeerList(driver, moodyalesUrl, waitFor, beerName)

    except:
        print('Error getMoodyales')

    driver.quit()

    return beerList

def getParkside():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="beer-drink-item"]'
        beerName = ['tr.beer-drink-item td.name']
        beerList = fillBeerList(driver, parksideUrl, waitFor, beerName)

    except:
        print('Error getParkside')

    driver.quit()

    return beerList

def getTwinsails():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="elementor-inner"]'
        beerName = ['div.elementor-widget-heading div.elementor-widget-container h1.elementor-heading-title']
        beerList = fillBeerList(driver, twinsailsUrl, waitFor, beerName)
        beerList = stripNewLine(beerList)
        beerList = spaceBeforeCapital(beerList)

    except:
        print('Error getTwinsails')

    driver.quit()

    return beerList
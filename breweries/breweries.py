from breweries.helpers import *

dageraadUrl = 'https://sites.google.com/dageraadbrewing.com/current-offerings/beers-on-tap'
yellowdogUrl = 'https://yellowdogbeer.com/tasting-room/'
moodyalesUrl = 'http://www.moodyales.com/'
parksideUrl = 'http://www.theparksidebrewery.com/tasting-room/'
twinsailsUrl = 'https://twinsailsbrewing.com/our-beers/'
frasermillsUrl = 'https://frasermillsfermentation.com/beer-menu/'


def getDageraad():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="zfr3Q"]'
        beerName = ['p[class="zfr3Q"] span[style="font-family: Open Sans; font-size: 12pt; font-style: normal; '
                    'text-decoration: normal; vertical-align: baseline;"]:nth-child(1)',
                    'p[class="zfr3Q"] span[style="font-family: Open Sans;"]:nth-child(1)']
        beerType = None
        beerList = fillBeerList(driver, dageraadUrl, waitFor, beerName, beerType)
        beerList = stripNonAlpha(beerList)
        beerList = stripNewLine(beerList)

    except:
        print('Error getDageraad')

    driver.quit()

    return beerList


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
        beerName = ['div.beers-ontap div.row div.col-md-12:nth-child(1) ul li a',
                    'div.beers-ontap div.row div.col-md-12:nth-child(1) ul li span']
        beerType = None
        beerList = fillBeerList(driver, moodyalesUrl, waitFor, beerName, beerType)

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
        beerType = None
        beerList = fillBeerList(driver, parksideUrl, waitFor, beerName, beerType)
        beerList = stripNonAlpha(beerList)

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
        beerType = None
        beerList = fillBeerList(driver, twinsailsUrl, waitFor, beerName, beerType)
        beerList = stripNewLine(beerList)
        beerList = spaceBeforeCapital(beerList)

    except:
        print('Error getTwinsails')

    driver.quit()

    return beerList


def getFrasermills():
    beerList = []
    driver = getChromeDriver()

    try:
        waitFor = '//*[@class="beer-name"]'
        beerName = ['div.tab-content#menu-77578 div.beer div.beer-details p.beer-name a.item-title-color']
        beerType = 'div.tab-content#menu-77578 div.beer div.beer-details p.beer-name span.beer-style'
        beerList = fillBeerList(driver, frasermillsUrl, waitFor, beerName, beerType)
        beerList = stripNewLine(beerList)
        beerList = stripNonAlpha(beerList)

    except RuntimeError:
        print('Error getFrasermills')

    driver.quit()

    return beerList

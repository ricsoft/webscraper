import { By } from "selenium-webdriver";
import { sleep, getDate } from "../utils/utils.js";

export default async function getNintendo(driver) {
  try {
    await driver.get(
      "https://www.nintendo.com/en-ca/store/games/best-sellers/#topLevelFilters=Deals&corePlatforms=Nintendo+Switch&f=topLevelFilters%2CcorePlatforms&sort=df"
    );
    await sleep(1);

    const titles = await driver.findElements(
      By.xpath(
        "//div[contains(@class, 'tilestyles__TitleWrapper-sc')]//h2[contains(@class, 'Textstyles__StyledTitle-sc')]"
      )
    );

    const prices = await driver.findElements(
      By.xpath(
        "//span[contains(@class, 'Pricestyles__ScreenReaderOnly-sc') and contains(text(), 'Current Price:')]/parent::span"
      )
    );

    if (titles.length !== prices.length) throw new Error("Count Mismatch");

    const data = [];
    let title = "";
    let price = "";

    for (let i = 0; i < titles.length; i++) {
      title = await titles[i].getText();
      price = await prices[i].getText();
      price = price.replace("Current Price:\n", "");
      data.push({ title: title, price: price });
    }

    return { site: "nintendo", lastUpdated: getDate(), data: data };
  } catch (e) {
    console.log("Nintendo Error", e);
    return null;
  }
}

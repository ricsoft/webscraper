import { By, until } from "selenium-webdriver";
import { sleep, getDate } from "../utils/utils.js";

export default async function getPlaystation(driver) {
  try {
    await driver.get(
      "https://store.playstation.com/en-ca/category/dc464929-edee-48a5-bcd3-1e6f5250ae80/1?PS5=targetPlatforms&FULL_GAME=storeDisplayClassification"
    );
    await sleep(1);

    let button = await driver.wait(
      until.elementLocated(
        By.xpath(
          "//button[contains(@class, 'ems-sdk-grid-sort-filter-tablet-margin')]"
        )
      )
    );
    button.click();

    button = await driver.wait(
      until.elementLocated(
        By.xpath(
          "//button[contains(@data-qa, 'ems-sdk-collapsible-menu--sort')]"
        )
      )
    );
    button.click();

    button = await driver.wait(
      until.elementLocated(
        By.xpath("//span[contains(@class, 'psw-radio-group')]//label[2]")
      )
    );
    button.click();
    await sleep(2.5);

    const titles = await driver.findElements(
      By.xpath(
        "//span[@class='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2']"
      )
    );

    const prices = await driver.findElements(
      By.xpath(
        "//div[@class='psw-l-line-left-top psw-l-line-wrap psw-clip psw-t-h-body-1']//span[@class='psw-m-r-3']"
      )
    );

    if (titles.length !== prices.length) throw new Error("Count Mismatch");

    const data = [];
    let title = "";
    let price = "";

    for (let i = 0; i < titles.length; i++) {
      title = await titles[i].getText();
      price = await prices[i].getText();
      data.push({ title: title, price: price });
    }

    return { site: "playstation", lastUpdated: getDate(), data: data };
  } catch (e) {
    console.log("Playstation Error", e);
    return null;
  }
}

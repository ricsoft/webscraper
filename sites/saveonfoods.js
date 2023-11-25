import { By } from "selenium-webdriver";
import { sleep, getDate } from "../utils/utils.js";

export default async function getSaveonfoods(driver) {
  const data = [];
  let temp = {};
  let titles, prices, title, price;

  try {
    await driver.get(
      "https://www.saveonfoods.com/sm/pickup/rsid/1982/save-on-savers"
    );
    await sleep(2);

    const button = await driver.findElement(
      By.xpath(
        "(//div[contains(@class, 'ProductCarousel')])[1]//button[contains(@class, 'RightArrow')]"
      )
    );

    for (let i = 0; i < 18; i++) {
      titles = await driver.findElements(
        By.xpath(
          "(//div[contains(@class, 'ProductCarousel')])[1]//span[contains(@class, 'ProductCardTitle--')]//div[contains(@data-testid, '-ProductNameTestId')]"
        )
      );

      prices = await driver.findElements(
        By.xpath(
          "(//div[contains(@class, 'ProductCarousel')])[1]//span[contains(@class, 'ProductCardPrice--')]"
        )
      );

      if (titles.length !== prices.length) throw new Error("Count Mismatch");

      for (let i = 0; i < titles.length; i++) {
        title = await titles[i].getText();
        price = await prices[i].getText();
        if (title) {
          title = title.split(", ")[0];
          if (price) temp[title] = price;
        }
      }

      button.click();
      await sleep(1);
    }

    for (let [key, value] of Object.entries(temp)) {
      data.push({ title: key, price: value });
    }

    return { site: "saveonfoods", lastUpdated: getDate(), data: data };
  } catch (e) {
    console.log("Save on Foods Error", e);
    return null;
  }
}

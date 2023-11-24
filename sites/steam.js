import { By, until } from "selenium-webdriver";
import { getDate } from "../utils/utils.js";

export default async function getSteam(driver) {
  try {
    await driver.get(
      "https://store.steampowered.com/specials/?flavor=contenthub_newandtrending"
    );

    await driver.wait(
      until.elementLocated(
        By.xpath(
          "//div[@class='facetedbrowse_FacetedBrowseItems_NO-IP']//img[contains(@class, 'salepreviewwidgets_CapsuleImage')]"
        )
      )
    );

    const titles = await driver.findElements(
      By.xpath(
        "//div[@class='facetedbrowse_FacetedBrowseItems_NO-IP']//div[contains(@class, 'salepreviewwidgets_StoreSaleWidgetTitle')]"
      )
    );

    const prices = await driver.findElements(
      By.xpath(
        "//div[@class='facetedbrowse_FacetedBrowseItems_NO-IP']//div[contains(@class, 'salepreviewwidgets_StoreSalePriceBox')]"
      )
    );

    if (titles.length !== prices.length) throw new Error("Count Mismatch");

    const data = [];
    let title = "";
    let price = "";

    for (let i = 0; i < titles.length; i++) {
      title = await titles[i].getText();
      price = await prices[i].getText();
      price = price.replace("C$ ", "$");
      data.push({ title: title, price: price });
    }

    return { site: "steam", lastUpdated: getDate(), data: data };
  } catch (e) {
    console.log("Steam Error", e);
    return null;
  }
}

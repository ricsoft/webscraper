import getDriver from "./utils/webdriver.js";
import getSteam from "./sites/steam.js";

async function main() {
  const driver = getDriver();
  const steam = await getSteam(driver);
  await driver.quit();

  console.log(steam)
}

main();

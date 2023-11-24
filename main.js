import { getDriver } from "./utils/utils.js";
import getSteam from "./sites/steam.js";
import getPlaystation from "./sites/playstation.js";

async function main() {
  const driver = getDriver();
  const steam = await getSteam(driver);
  const playstation = await getPlaystation(driver);
  await driver.quit();
}

main();

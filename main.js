import { getDriver, sendData } from "./utils/utils.js";
import getSteam from "./sites/steam.js";
import getPlaystation from "./sites/playstation.js";
import getNintendo from "./sites/nintendo.js";
import getSaveonfoods from "./sites/saveonfoods.js";

async function main() {
  const driver = getDriver();

  const steam = await getSteam(driver);
  const playstation = await getPlaystation(driver);
  const nintendo = await getNintendo(driver);
  const saveonfoods = await getSaveonfoods(driver);

  await driver.quit();

  const sites = [steam, playstation, nintendo, saveonfoods];
  const data = sites.filter((site) => site);

  sendData(data);
}

main();

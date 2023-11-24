import webdriver from "selenium-webdriver";

export default function getDriver() {
  const driver = new webdriver.Builder().forBrowser("chrome").build();
  return driver;
}

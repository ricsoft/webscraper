import webdriver from "selenium-webdriver";

export function getDriver() {
  const driver = new webdriver.Builder().forBrowser("chrome").build();
  return driver;
}

export function getDate() {
  const date = new Date().toLocaleDateString("pt-PT");
  return date;
}

export async function sleep(seconds) {
  await new Promise((resolve) => setTimeout(resolve, seconds * 1000));
}

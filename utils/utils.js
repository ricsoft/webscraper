import webdriver from "selenium-webdriver";
import { Options } from "selenium-webdriver/chrome.js";

export function getDriver() {
  const options = new Options();
  options.addArguments("--window-size=1300,900");

  const driver = new webdriver.Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  return driver;
}

export function getDate() {
  const date = new Date().toLocaleDateString("pt-PT");
  return date;
}

export async function sleep(seconds) {
  await new Promise((resolve) => setTimeout(resolve, seconds * 1000));
}

export async function sendData(data) {
  const response = await fetch("http://localhost:8080/api/discounts/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    console.log("Send Data Error");
  }

  return;
}

import webdriver from "selenium-webdriver";
import * as firefox from "selenium-webdriver/firefox.js";

export function getDriver() {
  const options = new firefox.Options();
  options.addArguments("--width=1300");
  options.addArguments("--height=1000");
  options.addArguments("--headless");
  const driver = new webdriver.Builder()
    .forBrowser("firefox")
    .setFirefoxOptions(options)
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
  // process.env.NODE_TLS_REJECT_UNAUTHORIZED = 0;
  // const url = "https://localhost:8080/api/discounts/"

  const url = "http://localhost:8080/api/discounts/";

  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    console.log("Send Data Error");
  }

  return;
}

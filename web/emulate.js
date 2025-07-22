const { chromium, firefox, webkit } = require('playwright');

(async () => {
  const browsers = [chromium, firefox, webkit];
  const browserType = browsers[Math.floor(Math.random() * browsers.length)];
  const browser = await browserType.launch({ headless: false });
  const page = await browser.newPage();
  console.log("Visiting Wikipedia...");
  await page.goto('https://www.wikipedia.org');
  console.log("Typing 'cyber security'...");
  await page.fill('input[name=search]', 'cyber security');
  await page.keyboard.press('Enter');
  const wait = Math.floor(Math.random() * 5000) + 3000;
  console.log(`Waiting ${wait} ms...`);
  await page.waitForTimeout(wait);
  await browser.close();
  console.log("Done!");
  const fs = require('fs');
  fs.appendFileSync('../logs/web_emulation.log', `${new Date().toISOString()} - Visited Wikipedia\n`);
})();

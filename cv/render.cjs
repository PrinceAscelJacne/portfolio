const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2]);
  const h = await p.evaluate(() => [document.querySelector('.main').scrollHeight, document.querySelector('.side').scrollHeight, document.querySelector('.page').clientHeight]);
  console.log('heights main/side/page', h);
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();

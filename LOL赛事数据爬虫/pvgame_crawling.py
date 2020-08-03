import asyncio
from pyppeteer import launch
from time import sleep

async def main():
    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    # await page.evaluate("""
    #     () =>{
    #         Object.defineProperties(navigator,{
    #             webdriver:{
    #             get: () => false
    #             }
    #         })
    #     }
    # """)
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto('https://www.vpgame.com/schedule')
    # data = await page.Jx('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/span')
    # for item in data:
    #     title_str1 = await (await item.getProperty('textContent')).jsonValue()
    #     print(title_str1)
    content = await page.Jx('//*[@id="root"]/div/div[1]/div[2]/div/ul/li[3]/a/span')
    await content[0].click()
    print(await page.content())
    sleep(10)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
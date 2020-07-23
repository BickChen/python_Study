import asyncio
from pyppeteer import launch
from lxml import etree

async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto('https://www.vpgame.com/schedule')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    lol = await page.Jx('//*[@id="root"]/div/div[1]/div[2]/div/ul/li[3]/a/span')
    await lol[0].click()
    await asyncio.sleep(2)

    match_info = await page.Jx('//*[@id="Schedule"]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div')
    await match_info[0].click()
    await asyncio.sleep(2)

    match_screen = await page.Jx('//*[@id="league-list"]/div[1]/div/div')
    await match_screen[0].click()
    await asyncio.sleep(2)

    match_list = await page.Jx('//*[@style="overflow: auto; transform: translateZ(0px);"]/ul/li')
    await match_list[1].click()
    await asyncio.sleep(2)

    start_Button = await page.Jx('//*[@id="deteSelect"]/span/span/i')
    await start_Button[0].click()
    await asyncio.sleep(2)
    await page.evaluate('document.querySelector("#deteSelect > div > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-range-part.ant-calendar-range-left > div.ant-calendar-input-wrap > div > input").value="2020/06/05"')
    # await page.type('#deteSelect > div > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-range-part.ant-calendar-range-left > div.ant-calendar-input-wrap > div > input', '2020/06/05')
    await asyncio.sleep(2)

    # start_time = await page.Jx('//*[@id="deteSelect"]/span/span/input[1]')
    # await start_time[0].click()

    # end_time = await page.Jx('//*[@id="deteSelect"]/div/div/div/div/div/div[1]/div[2]/div[1]/div/input')
    # page_text = await page.content()
    # tree = etree.HTML(page_text)
    # data = tree.xpath('//*[@id="Schedule"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div/ul/li[2]/div/span[1]/text()')[0]
    # print(data)
    # div_list = tree.xpath('//*[@id="Schedule"]/div[3]/div[1]/div[2]/div[1]/div[1]//div')
    # num = 1
    # for dev in div_list:
    #     if  num >= 3:
    #         match_name = dev.xpath('./div/ul/li[1]/p/text() | ./div/ul/li[1]/div/span[2]/text()')
    #         if match_name:
    #             print(match_name[0], match_name[1])
    #     elif num == 2:
    #         match_time = dev.xpath('./text()')
    #         print(match_time[0])
    #     num +=1
    await asyncio.sleep(10)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
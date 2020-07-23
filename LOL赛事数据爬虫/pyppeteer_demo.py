import asyncio
from pyppeteer import launch
from lxml import etree
import json

async def main():

    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto('https://www.vpgame.com/schedule/sha/dota2/pro/webservice/schedule/list/all?&game_type=lol&start_date=1591286400&end_date=1595347200&status=end&league_id=57&as=1595470107377&cp=63f48069bae5730e47b419939ce166d5&t=1595470107378')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(2)

    page_text = await page.content()
    tree = etree.HTML(page_text)
    data = tree.xpath('/html/body/pre/text()')
    data_dic = json.loads(data[0])
    print(data_dic)
    print(type(data_dic))
    print(len(data_dic['data']))
    print(data_dic['data'][0])
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
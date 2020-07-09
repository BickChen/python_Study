import requests
from lxml import etree

if __name__ in '__main__':
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    img_data = requests.get(url=url, headers=headers).text
    tree = etree.HTML(img_data)
    chapter_list = tree.xpath('//div[@class="book-mulu"]/ul/li//text()')
    chapter_url_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a//@href')
    num = 0
    with open('三国演艺全集.txt', 'w', encoding='utf-8') as fp:
        for name in chapter_list:
            url = 'http://www.shicimingju.com' + chapter_url_list[num]
            num +=1
            url_data = requests.get(url=url, headers=headers).text
            chapter_tree = etree.HTML(url_data)
            data = chapter_tree.xpath('//p//text()')
            fp.write(name + ':' + '\n')
            for d in data:
                line_data = str(d).split("xa0")
                fp.write(line_data[-1]+'\n')
            print(name + '爬去完毕！')



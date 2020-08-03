import requests, json, pymongo, oss2, re
from fake_useragent import UserAgent
"""
python：Python 3.7.3
pip3 install requests
pip3 install oss2
pip3 install pymongo
pip3 install fake-useragent
"""

class PvGame_Match(object):


    def __init__(self):
        self.ua = UserAgent()
        self.game_type = 'lol'
        self.start_time = '1591200000'
        self.end_time = '1595260800'
        self.league_id = '57'

    def run(self):
        self.headers = {'User-Agent': self.ua.random,
                        'Referer': 'https://www.vpgame.com/schedule'}
        self.lol_match()
        # print(self.headers)

    def lol_match(self):
        url = 'https://dataservice-sec.vpgame.com/dota2/pro/webservice/schedule/list/all?interval=7&game_type=lol&start_date=1595260800&status=end'
        # params = {
        #     'game_type': self.game_type,    #赛事类型
        #     'start_date': self.start_time,  # 当前赛事开始时间
        #     'end_date': self.end_time,    # 当前赛事进行到的时间
        #     'status': 'end',
        #     'league_id': self.league_id,           # 赛事ID
        #     'as': '1595300094771',
        #     'cp': 'ec328e8c20ebab696818353b30cb5574',
        #     't': '1595300094771'
        # }
        session = requests.Session()
        response = session.get(url=url, headers=self.headers).json()
        print(len(response['data']))
        # self.match_list = response['data']
        # print(self.match_list)
        # print(len(self.match_list))

if __name__ in "__main__":
    PvGame_Match().run()

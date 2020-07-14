import requests, json, pymongo, oss2, re

class LOLMatchData(object):

    def __init__(self):
        self.endpoint = 'http://oss-cn-shanghai.aliyuncs.com/'
        self.auth = oss2.Auth('xxxxx', 'xxxxx')
        self.bucket = oss2.Bucket(self.auth, self.endpoint, 'xxxxx')
        self.client = pymongo.MongoClient('xxxxx')
        # self.tournament_list = 'https://data.pentaq.com/business_api/2018mar/tournament_list'
        # self.tournament_situation = 'https://data.pentaq.com/business_api/2018mar/tournament_situation'
        # self.tournament_most_ban = 'https://data.pentaq.com/business_api/2018mar/tournament_most_ban'
        # self.tournament_most_pick = 'https://data.pentaq.com/business_api/2018mar/tournament_most_pick'
        self.match_list = 'https://data.pentaq.com/business_api/2018mar/match_list'
        self.match_info = 'https://data.pentaq.com/business_api/2018mar/match_info'
        self.headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }



    def run(self):
        self.matchlistdata_obtain()

    def matchlistdata_obtain(self):
        """
        1、将赛事图片logo图片存入OSS
        2、将爬取的原始数据图片地址替换为阿里云OSS图片地址
        3、将修改过的数据存入mongodb数据库
        4、判断图片和数据是否在oss和mongo存在，存在则只写入self.match_data_list
        """
        mongodb = self.client['lol_match']
        persons = mongodb['match_list']
        self.match_data_list = []
        for i in range(1,6):
            params = {
                'tour': '76',
                'team': '',
                'patch': '',
                'begin': '',
                'page': i
            }
            url_data = requests.get(url=self.match_list, params=params, headers=self.headers).json()
            for num in range(0, len(url_data['matches'])):
                matches = url_data['matches'][num]
                # match_dic = {
                #     'bo': matches['bo'],
                #     'id': matches['id'],
                #     'lol_version': matches['lol_version'],
                #     'start_at': matches['start_at'],
                #     'team_a_name': matches['team_a_name'],
                #     'team_a_win': matches['team_a_win'],
                #     'team_b_name': matches['team_b_name'],
                #     'team_b_win': matches['team_b_win']
                # }
                # a_logo_url = matches['team_a_logo']
                # b_logo_url = matches['team_b_logo']
                # a_logo_data = requests.get(url=a_logo_url, headers=self.headers).content
                # b_logo_data = requests.get(url=b_logo_url, headers=self.headers).content
                # a_logo_path = 'log/' + a_logo_url.split('/')[-1]
                # b_logo_path = 'log/' + b_logo_url.split('/')[-1]
                # self.bucket.put_object(a_logo_path, a_logo_data)
                # self.bucket.put_object(b_logo_path, b_logo_data)
                for key in matches:
                    if re.match("^http.*?(jpeg|png)$", str(matches[key])):
                        img_url = matches[key]
                        img_path = ("/").join(img_url.split('/')[3:])
                        img_data = requests.get(url=img_url, headers=self.headers).content
                        self.bucket.put_object(img_path, img_data)
                        matches[key] = 'https://lolmatchimg.oss-cn-shanghai.aliyuncs.com/' + img_path
                print(matches)

                self.match_data_list.append(matches)
        persons.insert_many(self.match_data_list)

    # def detailsdata_obtain(self):
    #     self.game_id = []
    #     if self.match_data_list:
    #         for i in self.match_data_list:
    #             params = {
    #                 'match': i['id']
    #             }
    #             url_data = requests.get(url=self.match_info, params=params, headers=self.headers).json()


if __name__ in '__main__':
    LOLMatchData().run()

